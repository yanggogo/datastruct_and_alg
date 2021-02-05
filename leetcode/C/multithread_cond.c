#include <pthread.h>

extern void printFoo();
extern void printBar();

typedef struct {
    int n;
    bool flag;
    pthread_mutex_t lock;
    pthread_cond_t cond;
} FooBar;

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*) malloc(sizeof(FooBar));
    obj->n = n;
    obj->flag = true;
    pthread_mutex_init(&obj->lock, NULL);
    pthread_cond_init(&obj->cond, NULL);
    
    // obj->lock = PTHREAD_MUTEX_INITIALIZER;
    // obj->cond = PTHREAD_COND_INITIALIZER;
    return obj;
}

void foo(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        
        // printFoo() outputs "foo". Do not change or remove this line.
        pthread_mutex_lock(&obj->lock);

        // 等待的条件为false，调用以下语句后
        while (!obj->flag)
        {
            // 调用pthread_cond_wait有两个效果：
            // 1. 当前线程阻塞，直到其他线程pthread_cond_signal(&obj->cond, &obj->lock)后，本函数才返回
            // 2. 释放obj->lock锁 ————> pthread_cond_wait内部会释放锁，当该线程被唤醒，又会自动获取锁
            pthread_cond_wait(&obj->cond, &obj->lock);
        }
        printFoo();
        obj->flag = false;
        pthread_cond_signal(&obj->cond);
        pthread_mutex_unlock(&obj->lock);
    }
}

void bar(FooBar* obj) {
    
    for (int i = 0; i < obj->n; i++) {
        
        pthread_mutex_lock(&obj->lock);
        // printBar() outputs "bar". Do not change or remove this line.
        while (obj->flag)
        {
            pthread_cond_wait(&obj->cond, &obj->lock);
        }
        printBar();
        obj->flag = true;
        pthread_cond_signal(&obj->cond);
        pthread_mutex_unlock(&obj->lock);
    }
}

void fooBarFree(FooBar* obj) {
    pthread_mutex_destroy(&obj->lock);
    pthread_cond_destroy(&obj->cond);
    free(obj);
    obj = NULL;
}

// question
// 1. 条件变量总是和锁一起使用
// 2. 如果初始化的时候，Bar先获得锁，是不是就死锁了？
// 3. foo 函数会不会再次抢到锁，导致死循环？


// 使用条件变量需要初始化三个变量：
// 1. 定义一个条件                      ———— 用于业务逻辑
// 2. 定义一个修改该条件的互斥量（锁）    ———— 用于互斥的修改条件
// 3. 定义一个条件变量（pthread_cond_t） ———— 用于线程间signal和线程阻塞