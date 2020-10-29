import numpy as np

#from nn_est import nn_train
from weight_est import kitekan_est, functions, virtual_sub

if __name__ == '__main__':
  '''
  factor_train = "./nn_est/data/test_input.csv"
  face_train = "./nn_est/data/test_output.csv"
  model_filename = "./nn_est/data/model_test.h5"
  data_path = "./nn_est/data"
  nn_train.nn_train(factor_train,face_train,model_filename,data_path)
  print('predict',nn_train.nn_predict(factor_train,model_filename))
  print('ans',face_train)
  '''

  import matplotlib.pyplot as plt
  for i in range(50):
    dim = 10 
    ans_length = 100
    noiz_order = -5.0

    ans_weight = np.random.randint(-10,10,(dim,))/10.0
    ans_x = np.random.rand(ans_length,dim)

    phi_t = functions.phi_quiz
    phi_ans = functions.phi_quiz

    train_time_length = 10
    test_time_length = 10

    train_id = np.sort(np.random.randint(0,ans_length,(train_time_length,)))

    train_factor = ans_x[train_id,:]
    train_face = virtual_sub.add_noiz(virtual_sub.out_virtual_data(phi_ans,ans_weight,train_factor),noiz_order)

    trained_w = kitekan_est.fit(phi_t,train_factor,train_face)
    print('train factor',train_factor[0,:])

    test_id = np.sort(np.random.randint(0,49,(test_time_length,)))
    test_factor = ans_x[test_id,:]

    estimated_ylist = virtual_sub.out_ydata(phi_t,trained_w,test_factor)

    plt.subplot(dim+1,1,1)
    plt.scatter(test_id,estimated_ylist,label="estimated_y")
    plt.scatter(train_id,train_face,label="trained_y")
    plt.plot(range(ans_length),virtual_sub.out_ydata(phi_ans,ans_weight,ans_x),label="answer")
    plt.legend(loc='center left', bbox_to_anchor=(1., .5))  

    for d in range(dim):
      plt.subplot(dim+1,1,d+2)
      plt.scatter(test_factor[:,d],estimated_ylist,label="estimated_y")
      plt.scatter(train_factor[:,d],train_face,label="trained_y")
      plt.ylabel('y'+str(d+1))
      plt.scatter(ans_x[:,d],virtual_sub.out_ydata(phi_ans,ans_weight,ans_x),label="answer",facecolors='none',edgecolors='gray')
      plt.legend(loc='center left', bbox_to_anchor=(1., .5))  



    print('tra x,tes x',train_factor,test_factor)
    print('weight compare',ans_weight,trained_w)
    tra=np.array([virtual_sub.out_ydata(phi_ans,trained_w,test_factor)])
    ans=np.array([virtual_sub.out_ydata(phi_t,ans_weight,test_factor)])
    print('diff sum',np.sum(ans-tra))

    plt.show()

  '''
  ff=train_factor
  noize = np.random.rand(*ff.shape)
  print(noize)
  test_factor = ff#+0.05*noize
  '''
