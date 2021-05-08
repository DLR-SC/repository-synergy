
**Introduction**

This is a Python routine for running Bundler and PMVS(CMVS). Which was origin from [https://code.google.com/p/osm-bundler/][1]. This routine facility the  Structure From motion procedure with Bundler and Prepare the required data structure for running PMVS, which is a opensource dense reconstruction software.


**Usage**

You are supposed to put the requred software in the *software* directory , 

 - bundler
 - pmvs
 - sift-lowe (or vlfeat)
  
the structure may like below:

    software
    ----bundler
            Bundle2Ply   
            Bundle2Vis  
            KeyMatchFull    
            RadialUndistort
            Bundle2PMVS  
            bundler     
            libANN_char.so

    ----pmvs
            cmvs  
            genOption  
            pmvs2

    ----sift-lowe
            sift
            
 
 **Note for Linux**
 
 remember to set `LD_LIBRARY_PATH` to `libANN_char.so` ,otherwise KeyMatchFull may not find the library and crash

Run this procedure:
Perform point cloud and camera calibration :

    $ RunBundler.py --photos="./examples/MyPhotos" 

**Note:** The default output will be in the *output* directory in the root of the osm-bundler .
You could test various option... 
    
    $ RunBundler.py

In a second step you could compute the dense 3D point cloud in one step if the dataset have a reasonable size.

    $ RunPMVS.py --bundlerOutputPath="output of bundler" 
    
**Note:** bundlerOutputPath shoud be the bundler output directory.

If you have a lot of images, it better to use CMVS cluster computation.
It performs dense 3D point could computation by using Cluster 3D representation of the scene :

    $ RunCMVS.py --bundlerOutputPath="output of bundler" --ClusterToCompute ="Number of Desired Cluster".
    
Example :

    $ RunCMVS.py --bundlerOutputPath="C:/temp/osm-Result" --ClusterToCompute ="10".


**Other reference**

Bundler: [http://www.cs.cornell.edu/~snavely/bundler/][2]  
  PMVS2: [http://grail.cs.washington.edu/software/pmvs/][3]  
   CMVS: [http://grail.cs.washington.edu/software/cmvs/][4]  


  [1]: https://code.google.com/p/osm-bundler/
  [2]: http://www.cs.cornell.edu/~snavely/bundler/
  [3]: http://grail.cs.washington.edu/software/pmvs/
  [4]: http://grail.cs.washington.edu/software/cmvs/
