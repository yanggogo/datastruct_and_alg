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
        while (!obj->flag)
        {
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

