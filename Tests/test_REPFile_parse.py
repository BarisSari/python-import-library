import os, sys
import unittest
import datetime

from Formats.REPFile import REPFile, REPLine
from Formats.Location import Location

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    def setUp(self):
        pass

    def tearDown(self):
        pass

    ####################
    #### line tests ####
    ####################

    def test_LongTimeStamp(self):
        # long date
        repline = REPLine(1, "19951212 120800 SUBJECT VC 60 23 40.25 N 000 01 25.86 E 109.08  6.00  0.00 ")
        repline.parse()

        # long time
        repline = REPLine(1, "951212 120800.555 SUBJECT VC 60 23 40.25 N 000 01 25.86 E 109.08  6.00  0.00 ")
        repline.parse()

    def test_Getters(self):
        repline = REPLine(1, "951212 120800.555 SUBJECT VC 60 23 40.25 N 000 01 25.86 E 109.08  6.00  0.00 ")
        repline.parse()

        repline.getLineNum
        repline.getTimestamp
        repline.getPlatform
        repline.getSymbology
        repline.getLatitude
        repline.getLongitude
        repline.getHeading
        repline.getSpeed
        repline.getDepth
        repline.getTextLabel

    def test_ErrorReports(self):
        # too few fields
        repline = REPLine(1, " 23 40.25 N 000 01 25.86 E 109.08  6.00  0.00 ")
        repline.parse()

        # wrong length date
        repline = REPLine(1, "12 120800 SUBJECT VC 60 23 40.25 N 000 01 25.86 E 109.08  6.00  0.00 ")
        repline.parse()

        # wrong length time
        repline = REPLine(1, "951212 12 SUBJECT VC 60 23 40.25 N 000 01 25.86 E 109.08  6.00  0.00 ")
        repline.parse()

        # wrong length symbology
        repline = REPLine(1, "951212 120800 SUBJECT VCC 60 23 40.25 N 000 01 25.86 E 109.08  6.00  0.00 ")
        repline.parse()

        # bad latitude
        repline = REPLine(1, "951212 120800 SUBJECT VC 6A 23 40.25 N 000 01 25.86 E 109.08  6.00  0.00 ")
        repline.parse()

        # bad longtude
        repline = REPLine(1, "951212 120800 SUBJECT VC 60 23 40.25 N 00A 01 2B.86 E 109.08  6.00  0.00 ")
        repline.parse()

        # bad course
        repline = REPLine(1, "951212 120800 SUBJECT VC 60 23 40.25 N 000 01 25.86 E 10a.08  6.00  0.00 ")
        repline.parse()

        # bad speed
        repline = REPLine(1, "951212 120800 SUBJECT VC 60 23 40.25 N 000 01 25.86 E 109.08  6.b0  0.00 ")
        repline.parse()

        # bad depth
        repline = REPLine(1, "951212 120800 SUBJECT VC 60 23 40.25 N 000 01 25.86 E 109.08  6.00  0.c0 ")
        repline.parse()



    def test_lineOk(self):
        repline = REPLine(1, "100112 120800 SUBJECT VC 60 23 40.25 N 000 01 25.86 E 109.08  6.00  0.00 ")
        repline.parse()

        self.assertEqual(1, repline.getLineNum())

        print(repline.getTimestamp())

        self.assertEqual(datetime.datetime(2010, 1, 12, 12, 8), repline.getTimestamp())
        self.assertEqual("SUBJECT", repline.getPlatform())
        self.assertEqual("VC", repline.getSymbology())
     #FixMe   self.assertEqual(Location(60.0, 23.0, 40.25, "N"), repline.getLatitude())
     #FixMe   self.assertEqual("SUBJECT", repline.getLongitude())
        self.assertEqual(109.08, repline.getHeading())
        self.assertEqual(6.0, repline.getSpeed())
        self.assertEqual(0.0, repline.getDepth())
        self.assertEqual(None, repline.getTextLabel())

if __name__ == "__main__":
    unittest.main()
