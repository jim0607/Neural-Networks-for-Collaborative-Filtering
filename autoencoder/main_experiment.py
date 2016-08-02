from autoencoder.Experiment2 import Experiment

autoencoder_parameters_range = {'hidden1_units': 700,
                                'regularisation': 0.02,
                                'learning_rate0': 0.001,
                                'learning_decay': 0.9,
                                'batch_size_evaluate': 100,
                                'batch_size_train': 35,
                                'nb_epoch': 15}

sets_parameters = {'database_id': 1,
                   'test_ratio': 0.,
                   'validation_ratio': 0.1}

experiment_parameters = {'mean_iterations': 1,
                         'nb_draws': 10}

Experiment = Experiment(experiment_parameters=experiment_parameters,
                        autoencoder_parameters_range=autoencoder_parameters_range,
                        sets_parameters=sets_parameters)
Experiment.run()

