# Joint Embeddings of Shapes and Images via CNN Image Purification
Created by <a href="http://web.stanford.edu/~yangyan/" target="_blank">Yangyan Li</a>, <a href="http://ai.stanford.edu/~haosu/" target="_blank">Hao Su</a>, <a href="http://web.stanford.edu/~rqi/" target="_blank">Charles Ruizhongtai Qi</a>, <a href="http://geometry.stanford.edu/member/guibas/" target="_blank">Leonidas J. Guibas</a> from Stanford University, and <a href="http://www.cs.tau.ac.il/~noafish/" target="_blank">Noa Fish</a>, <a href="http://www.cs.tau.ac.il/~dcor/" target="_blank">Daniel Cohen-Or</a> from Tel Aviv University.

### Introduction
We propose a way to embed 3D shapes and 2D images into a joint embedding space, thus all of the 3D shapes and 2D images become searchable from each other (<a href="https://shapenet.cs.stanford.edu/shapenet_brain/app_joint_embedding/" target="_blank">live demo</a>). The <a href="https://shapenet.cs.stanford.edu/projects/JointEmbedding/" target="_blank">research paper</a> was accepted to SIGGRAPH Asia 2015.

### License
JointEmbedding is released under the 4-clause BSD license (the original "BSD License", refer to the LICENSE file for details).

### Citing JointEmbedding
If you find JointEmbedding useful in your research, please consider citing:

    @article{li2015jointembedding,
        Author = {Li, Yangyan and Su, Hao and Qi, Charles Ruizhongtai and Fish, Noa
            and Cohen-Or, Daniel and Guibas, Leonidas J.},
        Title = {Joint Embeddings of Shapes and Images via CNN Image Purification},
        Journal = {ACM Trans. Graph.},
        Year = {2015}
    }
    
## Contents
### 1. Usage: How to test with trained models?
The trained model for chair category (03001627) can be downloaded from <a href="https://shapenet.cs.stanford.edu/projects/JointEmbedding/data/03001627.zip" target="_blank">here</a>. You can try them with script `extract_image_embedding.py` and `image_based_shape_retrieval.py` in `src/image_embedding_testing folder`, with the following commands: 

    extract_image_embedding.py --image YOUR_TESTING_IMAGE --caffemodel image_embedding_03001627.caffemodel  --prototxt image_embedding_03001627.prototxt
    image_based_shape_retrieval.py --image YOUR_TESTING_IMAGE --caffemodel image_embedding_03001627.caffemodel  --prototxt image_embedding_03001627.prototxt

### 2. Usage: How to train your own models?
#### 2.1. Requirements: datasets
+ ShapeNetCore is used for constructing the shape embedding space and generating synthetic images. Visit The <a href="http://shapenet.org/" target="_blank">shapenet.org</a>, and request to download the ShapeNetCore dataset. ShapeNetCore.v1 (also called ShapeNetCore2015Summer) is prefered (there were many broken meshes in ShapeNetCore.v0/ShapeNetCore2015Spring).
+ <a href="http://groups.csail.mit.edu/vision/SUN/" target="_blank">SUN2012</a> dataset is used for background overlay of the synthetic images. Will be downloaded by our script.

#### 2.2. Requirements: software
+ <a href="http://caffe.berkeleyvision.org/" target="\_blank">Caffe</a> is used for deep learning. Install it (including the pycaffe module) by following their instructions. You are required to specify your caffe installation path in `global_varialbes.py`.
+ <a href="https://www.blender.org/" target="_blank">Blender</a> is used for rendering shapes into images. Will be downloaded by our script.
+ Matlab. You are required to specify matlab executable path in `global_varialbes.py`.
+ <a href="https://github.com/pdollar/toolbox" target="_blank">Piotr's Image & Video Matlab Toolbox</a> is used for HoG feature extraction. Will be downloaded by our script.

#### 2.3. Requirements: hardware
+ Highend GPU(s) are required for the deep learning part.
+ You may also need highend CPU(s), as millions of images will be rendered, processed.

#### 2.4. Installation
The code is written by python, matlab and shell. There is no need for any installation of the code itself. Just:

    git clone https://github.com/ShapeNet/JointEmbedding.git JointEmbedding;
    cd JointEmbedding/src;
    cp default_global_variables.py global_variables.py
    
#### 2.5. Run the pipeline
1. Edit `global_variables.py`, especially the ones marked by **[take care!]**
2. Execute `run_preparation.sh`. It will download some 3rd party software, and prepare shell scripts for next steps.
3. Execute `run_shape_embedding_training.sh` to generate shape embedding space.
4. Execute `run_image_embedding_training.sh` to generate synthetic images.
5. Execute `run_joint_embedding_training.sh` to prepare and start the actual process.

##### Notes
1. You can run step 3 and 4 in parallel, well, in different machines, since both of them are multi-threaded, and you won't gain much speedup if you run them in parallel in the same machine.
2. Step 3, 4, and 5 are also very I/O intensive, try large SSD if you have.
3. The `run_\*.sh` scripts further divided the tasks into smaller tasks. Feed `-f first_step -l last_step` parameters to the `run_\*.sh` scripts to run part of them.
3. Read the scripts, starting from the `run_\*.sh`, to get more understanding of the code and build upon it!

### 3. Questions?
Refer to [Frequently Asked Questions](https://github.com/ShapeNet/JointEmbedding/wiki/Frequently-Asked-Questions) first.
