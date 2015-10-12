import unittest, os, sys
from blackjack.cmake.storage.file.ScriptBlock import ScriptBlock

class Test_ScriptBlock(unittest.TestCase):

    def setup_block(self):
        contentsparam = ["#middle1", "#middle2"]
        block1 = ScriptBlock(contentsparam)
        block1.Header.append("#header1")
        block1.Header.append("#header2")
        block1.Footer.append("#footer1")
        block1.Footer.append("#footer2")
        block1.Body.append("#middle3")
        return block1

    def test_render(self):
        block1 = self.setup_block()
        outputraw = block1.render_string()
        result = outputraw.splitlines()
        print(result)
        if result != ['#header1', '#header2', '#middle1', '#middle2', '#middle3', '#footer1', '#footer2']:
            self.fail("Unexpected Output")
        return

    def test_importfile_export(self):
        block1 = self.setup_block()
        block1.export()
        block2 = ScriptBlock()
        block2.importfile(block1.OutputFilePath)
        os.remove(block1.OutputFilePath)

        outputraw = block2.render_string()
        result = outputraw.splitlines()
        print(result)
        if result != ['#header1', '#header2', '#middle1', '#middle2', '#middle3', '#footer1', '#footer2']:
            self.fail("Unexpected Output")        
        return

if __name__ == '__main__':
    unittest.main()
