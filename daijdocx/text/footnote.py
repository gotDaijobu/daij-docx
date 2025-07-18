from ..shared import Parented
from ..text.paragraph import Paragraph

class Footnote(Parented):
    """A wrapper for a footnote element, similar to Comment."""
    def __init__(self, footnote, parent):
        super().__init__(parent)
        self._footnote = self._element = self.element = footnote

    @property
    def paragraph(self):
        return self.element.paragraph
    
    @property
    def text(self):
        # Return the concatenated text of all <w:t> elements in the first paragraph
        p = self.element.p
        if p is not None:
            t_elems = p.findall('.//w:t', {'w': p.nsmap['w']})
            full_text = []
            for t_elem in t_elems:
                parent = t_elem.getparent()
                is_in_hyperlink = False
                while parent is not None:
                    if parent.tag == '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hyperlink':
                        is_in_hyperlink = True
                        break
                    parent = parent.getparent()
                if not is_in_hyperlink:
                    full_text.append(t_elem.text or '')
                else:
                    full_text.append((t_elem.text or '') + ' (hyperlink)')
            return ''.join(full_text)
        return ""

    @text.setter
    def text(self, text):
        # Merge all non-hyperlink <w:t> into a single <w:t> in the first paragraph, preserving hyperlinks
        p_list = self.element.findall('.//w:p', {'w': self.element.nsmap['w']})
        if not p_list:
            return
        first_p = p_list[0]
        # Gather all non-hyperlink <w:t> elements
        t_elems = []
        text = text
        for p in p_list:
            for t_elem in p.findall('.//w:t', {'w': self.element.nsmap['w']}):
                parent = t_elem.getparent()
                is_in_hyperlink = False
                while parent is not None:
                    if parent.tag == '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hyperlink':
                        is_in_hyperlink = True
                        break
                    parent = parent.getparent()
                if not is_in_hyperlink:
                    t_elems.append(t_elem)
        if t_elems:
            t_elems[0].text = text
            for t_elem in t_elems[1:]:
                t_elem.text = ''

    @property
    def id(self):
        """Return the id of the footnote as an integer."""
        return int(self.element.get("w:id") or self.element.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}id"))
