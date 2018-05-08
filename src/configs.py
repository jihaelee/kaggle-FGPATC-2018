# -*- coding: utf-8 -*-

config1 = {
        'sampling_rate': 16000,
        'audio_duration': 2,
        'batch_size': 64,
        'n_classes': 41,
        'use_mfcc': False,
        'n_mfcc': 20,
        'n_folds': 10,
        'learning_rate': 0.001,
        'max_epochs': 50,
        'optimizer': 'sgd',
        'audio_pad_method': 'constant',
        'data_dir': '../data/freesound-audio-tagging/',
        'log_dir': '../logs/',
        'tmp_dir': '../tmp/'
}
