# Copyright (c) 2010 Anil Kumar
# All rights reserved.
#
# License: BSD 

__all__ = ["CallView", "ClassGraphView", "FileFuncGraphView", "EdView", "FileView", "ResView", "ProjectUi"]

def load_plugins():
	import seascope.view.filecontext
	filecontext.load_plugins()
