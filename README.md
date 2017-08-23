# FIBA_LineupData

Creates lineup data from the FIBA website Play by Play<br>
This script extracts play by play from the FIBA website using BeautifulSoup and creates a csv file containing lineups for each event in the PBP.<br>
This should work for any of the national team tournaments on the FIBA website.<br>
# Variables:
Game URL<br>
(example: http://www.fiba.basketball/asiacup/2017/0908/China-Philippines)<br>
<br>
Team/Country Trigram<br>
(example: CHN | PHI )
<br>
# Requirements
Python 3<br>
BeautifulSoup
<br>
# To Do
Code was created in a rush and can likely be simplified and tidied further.<br>
Country trigrams are available in the HTML which would mean this could be automatically added, rather than manually.<br>
Not all statistics are currently being extract - at this stage only stats required to create a basic possession calculation have been included.
