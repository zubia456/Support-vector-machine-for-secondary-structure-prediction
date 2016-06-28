# Support-vector-machine-for-secondary-structure-prediction
Instruction for using libsvm
For trainig the model we need to run the following command. For example  in order to train our model with the training data for C classifier the command will look like the following
libsvm-3.21_RJZ/svm-train -s 1 -t 2 -nu 0.25 C.training C.nu.model
following parameters are being used in it
•	s = 1 nu sv(multi class Classifier)
•	t = 2(kernel type radial basis function)
•	nu with threshold 0.25
•	C.training = training data for C classifier
•	C.nu.model = model being trained
predicting the new labels based upon the learned model from previous step
libsvm-3.21_RJZ/svm-predict C.validation C.nu.model C.nu.out > C.nu.margines


