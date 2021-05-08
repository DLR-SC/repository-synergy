# Flasked-Notebooks

Proof of concept for dynamically rendering IPython Notebooks using Flask:

 - Unlike `nbviewer` each code cell in a notebook is executed on request.
 - Input variables can be injected to a notebook before executed it. 
 - Running `app.py` starts the flask site which renders the markdown and updated code output cells.
 - Notebooks are rendered within the existing flask site using the normal templating approach. 
 - Pages can be developed by starting the IPython Notebook server in the `notebooks` directory.

 
**Next steps:**

Dynamically executing and rendering notebooks that use Widgets for interactive pages.

**Contributing:**

Ideas on better ways to do this, feedback and pull requests all welcome!
