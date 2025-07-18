Daij-docx
==========

Python library forked from [python-docx](https://github.com/python-openxml/python-docx and Bayoo-docx

The main purpose of the fork was to add implementation for comments and footnotes to the library

Installation
------------

Use the package manager pip to install daij-docx.


`pip install git+https://github.com/gotDaijobu/bayoo-docx`

Usage:
-----


    
    import docx
    
    document = docx.Document()

    paragraph = document.add_paragraph('text') # create new paragraph

    comment = paragraph.add_comment('comment',author='Obay Daba',initials= 'od') # add a comment on the entire paragraph

    paragraph2 = document.add_paragraph('text') # create another paragraph

    run = paragraph2.add_run('text1') #add a run to the paragraph

    run.add_comment('comment') # add a comment only for the run text 

    run.add_comment('comment2')

    run_comments = run.comments

    paragraph.add_footnote('footnote text') # add a footnote


