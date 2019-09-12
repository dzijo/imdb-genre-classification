import fasttext

model = fasttext.train_supervised('dataset_train.txt', lr = 0.04, dim = 100, ws = 5, epoch = 200, minCount = 4)
