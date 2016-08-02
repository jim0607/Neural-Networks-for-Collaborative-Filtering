from autoencoder.Train import Train
import numpy as np
from tools import to_dense


class TrainStability(Train):
    def __init__(self, database, Train_set, batch_size, learning_rate0, learning_decay):
        super().__init__(database, Train_set, batch_size, learning_rate0, learning_decay)

    def fill_feed_dict_train_stability(self, target, x_sparse, coefficients, learning_rate):
        x_sparse_indices, x_sparse_values, coefficients_indices, coefficients_values = self.Train_set.next_batch_train_stability(self.batch_size,
                                                                                                                 name='user')
        shape = np.array([self.batch_size, self.nb_movies], dtype=np.int64)
        feed_dict = {
            target: to_dense(x_sparse_indices, x_sparse_values, shape),
            x_sparse: (x_sparse_indices, x_sparse_values, shape),
            coefficients: to_dense(coefficients_indices, coefficients_values, shape),
            learning_rate: self.learning_rate
        }
        return feed_dict