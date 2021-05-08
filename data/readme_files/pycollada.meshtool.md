# Installation

### Release

    pip install meshtool

### Development

    git clone git://github.com/pycollada/meshtool.git meshtool
    cd meshtool
    python meshtool --help

### Optional Dependencies

Some visualization filters use Panda3D. To enable the filters, install version 1.7.2 of the Panda3D SDK from here:
http://www.panda3d.org/download.php?sdk&version=1.7.2

# Examples

    $ python meshtool --load_collada duck.dae --print_textures
    ./duckCM.tga

# Usage and Filter List

    usage: meshtool --load_filter [--operation] [--save_filter]
    
    Tool for manipulating mesh data using pycollada.
    
    Loading:
      --load_collada file   Loads a collada file
      --load_obj file       Loads a Wavefront OBJ file
    
    Printing:
      --print_textures      Prints a list of the embedded images in the mesh
      --print_render_info   Prints estimated number of batches, total number of
                            triangles, and total texture memory
      --print_json          Prints a bunch of information about the mesh in a JSON
                            format
      --print_info          Prints a bunch of information about the mesh to the
                            console
      --print_instances     Prints geometry instances from the default scene
      --print_scene         Prints the default scene tree
      --print_bounds        Prints bounds information about the mesh
    
    Simplification:
      --sander_simplify pm_file
                            Simplifies the mesh based on sandler, et al. method.
      --add_back_pm pm_file percent
                            Adds back mesh data from a progressive PDAE file
    
    Optimizations:
      --combine_effects     Combines identical effects
      --combine_materials   Combines identical materials
      --combine_primitives  Combines primitives within a geometry if they have the
                            same sources and scene material mapping (triangle sets
                            only)
      --strip_lines         Strips any lines from the document
      --strip_empty_geometry
                            Strips any empty geometry from the document and
                            removes them from any scenes
      --strip_unused_sources
                            Strips any source arrays from geometries if they
                            aren't referenced by any primitives
      --triangulate         Replaces any polylist or polygons with triangles
      --generate_normals    Generates normals for any triangle sets that don't
                            have any
      --save_mipmaps        Saves mipmaps to disk in tar format in the same
                            location as textures but with an added .tar. The
                            archive will contain PNG or JPG images.
      --optimize_textures   Converts all textures with alpha channel to PNG and
                            ones without to JPEG
      --adjust_texcoords    Adjusts texture coordinates of triangles so that they
                            are as close to the 0-1 range as possible
      --normalize_indices   Goes through all triangle sets, changing all index
                            values to go from 1 to N, replacing sources to be size
                            N
      --make_atlases        Makes a texture atlas with the textures referenced in
                            the given file. Extremely conservative: will only make
                            an atlas from texture coordinates inside the range
                            (0,1). Atlas can be saved with --save_collada_zip.
      --split_triangle_texcoords
                            Splits triangles that span multiple texcoords into
                            multiple triangles to better help texture atlasing
      --optimize_sources    Compresses sources to unique values, updating
                            triangleset indices
    
    Visualizations:
      --viewer              Uses panda3d to bring up a viewer
      --collada_viewer      Uses panda3d to bring up a viewer with lights and
                            camera from the collada file
      --pm_viewer pm_file   Uses panda3d to bring up a viewer of a base mesh and
                            progressive stream
    
    Meta:
      --medium_optimizations
                            A meta filter that runs a safe, medium-level of
                            optimizations. Performs these filters in this order:
                            triangulate, generate_normals, combine_effects,
                            combine_materials, combine_primitives,
                            optimize_sources, strip_unused_sources,
                            optimize_textures
      --full_optimizations  A meta filter that runs all optimizations. Performs
                            these filters in this order: triangulate,
                            generate_normals, combine_effects, combine_materials,
                            combine_primitives, adjust_texcoords,
                            optimize_textures, split_triangle_texcoords,
                            normalize_indices, make_atlases, combine_effects,
                            combine_materials, combine_primitives,
                            optimize_sourcesstrip_unused_sources,
                            optimize_textures
    
    Saving:
      --save_screenshot file
                            Saves a screenshot of the rendered collada file
      --save_rotate_screenshots file N W H
                            Saves N screenshots of size WxH, rotating evenly
                            spaced around the object between shots. Each
                            screenshot file will be file.n.png
      --save_collada file   Saves a collada file
      --save_collada_zip file
                            Saves a collada file and textures in a zip file.
                            Normalizes texture paths.
      --save_badgerfish file
                            Saves a collada file as JSON badgerfish
      --save_ply file       Saves a collada model in PLY format
      --save_obj file       Saves a mesh as an OBJ file
      --save_obj_zip file   Saves an OBJ file and textures in a zip file.
                            Normalizes texture paths.
      --save_bam file       Saves to Panda3D BAM file format
      --save_threejs_scene file
                            Saves a collada model in three.js scene format
