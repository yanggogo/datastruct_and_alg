int maxScore(int* cardPoints, int cardPointsSize, int k){
    int sum = 0;
    int window_size = cardPointsSize - k;
    for (int i = 0; i < cardPointsSize; i++)
    {
        sum += cardPoints[i];
    }

    int tmp_window_sum = 0;
    for (int i = 0; i < window_size; i++)
    {
        tmp_window_sum += cardPoints[i];
    }

    int min_tmp_sum = tmp_window_sum;
    for (int i = window_size; i < cardPointsSize; i++)
    {
        tmp_window_sum = tmp_window_sum + cardPoints[i] - cardPoints[i-window_size];
        if (tmp_window_sum < min_tmp_sum)
        {
            min_tmp_sum = tmp_window_sum;
        }
    }
    return sum - min_tmp_sum;
}