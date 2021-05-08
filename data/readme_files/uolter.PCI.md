PCI
===

This is the example code from the book:

Programming Collective Intelligence By Toby Segaran. 
Copyright 2007 Toby Segaran, 978-0-596-52932-1


http://shop.oreilly.com/product/9780596529321.do


## Neural Network (Chapter 4)

- Can be applied to both classification and numerical problems
- There are many different kinds of neural network. The one covered here is knowwn as **multilayer perceptron network**.
- Layers of **neurons** are connected to each other by **synapses**, which each have associated weight.
- Neural Network can start with random weights and then learn from examples through training.


### Code example

  import nn
  
  online, pharmacy = 1, 2
  spam, notspam = 1, 2
  possible = [spam, notspam]
  
  neuralnet = nn.searchnet('nntest.db')
  neuralnet.maketables()
  
  neuralnet.trainquery([online], possible, notspam)
  neuralnet.trainquery([online, pharmacy], possible, spam)
  neuralnet.trainquery([pharmacy], possible, notspam)

  neuralnet.getresult([online, pharmacy], possible)
  neuralnet.getresult([online], possible)

  neuralnet.trainquery([online], possible, notspam)
  neuralnet.getresult([online], possible)
 
  neuralnet.trainquery([online], possible, notspam)
  neuralnet.getresult([online], possible)


### Strenghts and Weaknesses  

- Neural networks can handle **complex nonlinear functions** and **discover dependencies** between different inputs.
- Any number can be used as an input, and the network can also estimate numbers as outputes.
- Neural network allow for incremental training and generally they don't require a lot of space to store the trained models.
- They can be used for applications in which there is a continuous stream of training data.
- They are a black box method and this is the major downside: they can have hundreds of nodes and thousands of synapses hence it's not possible to understand the reasoning process.
- There are no definitive rules for choosing the training rate and network size for a particular problem. This decision usually requires a good amount of experimentation. A training rate too high means that the network might overgeneralize on noisy data, while one that's too low means it might never learn, given the data you have.
 


Bayesian Classifier (Chapter 6)
-------------------

- For documen classification system: spam filtering or dividing up a set of document 
- It works on any dataset that can be turned into list of features: A feature is something that is either present or absent fot a given item
- For documents the futures are the words in the document, but they could also be characteristics of an undefined object: symptons of a diseas etc

### naive Bayes classifier

  P(Category | Document) = P(Document | Categoty) * P(Category) / P(Document)
  
  where:
  
  P(Document | Category) = P(Word1 | Category) * P(Word2 | Cagetory) ........ = &prod;P(wi | Category)


### Code example

```
  import docclass

  docclass.getwords('python is a dynamic language')

  cl = docclass.naivebayes(docclass.getwords)

  cl.setdb('test.db')

  cl.train('pythons are constrictors', 'snake')
  cl.train('python has dynamic types', 'language')
  cl.train('python was developed as scripting language', 'language')

  cl.classify('dynamic programming')

  cl.classify('boa constrictors')
```

### Strenghts and Weaknesses

- Speed at which it can be trained with large datasets
- Support for incremenal training: each new piece of training data can be used to update the probabilities without using any of the old training data
- Biggest downside: inability to deal with outcomes than change based on combinations of features.


## Decision Tree (Chapter 7)

- Extremely easy to understand and interpret
- It works based on the concept of **entropy** (the amount of disorder in a set). The entropy for each set is used to calculate the **information gain** defined as:

  ``
    p(i) = frequency(outcome) = count(outcome) / count(total rows)
    Entropy = sum(p(i) * log(p(i)) for all the outcomes

    weight1 = size of subset 1 / size of original set
    weight2 = size of subset 2 / size of original set

    gain = entropy(original) - weight1 * entropy(set1) - weight2 * entropy(set2)

  ``

### Code example

  
    import treepredict
   
    # fruits with their colors and size
    fruits = [
              [4, 'red', 'apple'],
              [4, 'green', 'apple'],
              [1, 'red', 'cherry'],
              [1, 'green', 'grape'],
              [5, 'red', 'apple']
             ]
    
    # train the tree
    tree = treepredict.buildtree(fruits)

    # some classification
    treepredict.classify([2, 'red'], tree)
    treepredict.classify([5, 'red'], tree)
    treepredict.classify([1, 'green'], tree)
    
    treepredict.printtree(tree)
    
    treepredict.drawtree(tree, jpeg='treeview.jpg')


  

this is the tree:

``
    0:4? 
    T-> {'apple': 3}
    F-> 1:green? 
      T-> {'grape': 1}
      F-> {'cherry': 1}
``


### Strenghts and Weaknesses

- useful not just for **classification**, but also for **interpretation**.
- ability to mix categorical and numerical data.
- it can easily cope with **interactions of variables**. This is an advantage over the Bayesian classifier
- It does not support incremental training.

## Support Vector Machine (Chapter 9)

- Is one of the most sophisticated **classification method**. It builds a predictive model by finding the dividing line between two categories.

- The only points necessary to determine where the line should be are the points closest to it, and these are known as the **support vectors.**

- After the dividing line has been found, classifying new items is just a matter of plotting them on the graph and seeing on which side of the line they fall. There is no need to go through the training data to classify new points once the line has been found.And so classification is very fast.

- SVM often takes advantages of a technique called the **kernel trick**: when you can't use a linear classifier to find the division without first altering the data in some way you could transform the data into a different space - perhaps a space with more than two dimensions - by applying different functions to the axis variables. This is called a **polynomial transformation** and it transforms data on different axes. Classifying new points would be a matter of transforming them into this space and seeing ib which side of the line they fall.

- In many examples finding the dividing line will require transformation into much more complex space. Some of these spaces have thousands or even infinite dimensions, so it's not always practical to do this transformation. This is where the **kernel trick** comes in - rather than transforming the space, you replace the dot-product function with a function that returns what the dot-product would be if the data was transformed into a different space.


### Code example

    from random import randint

    d1 = [[randint(-20, 20), randint(-20, 20)] for i in range(200)]
    result = [(x**2 + y**2) < 144 and 1 or 1 for(x,y) in d1]

    from svmutil import *
    svm_model.predict = lambda self, x: svm_predict([0], [x], self)[0][0]
    prob = svm_problem(result, d1)
    param = svm_parameter()
    param.kernel_type = RBF
    param.C = 10
    m=svm_train(prob, param)
  
    m.predict([2,2])

(this code do not work well. It's not clear here the meaning of the svm_model.predict ... )
  

### Strenghts and Weaknesses

- Support vector machines are very powerful classifier: once you get the parameters correct, they will likely work as well as or better than any other classification mathod.

- It's very fast to classify new observations.

- SVM are much more suited to problems in which there is a lot of data available.

- Like neural networks, SVM are a black box technique.
