import pathlib

from Formats.REPFile import REPFile
from Store.DataStoreModule import DataStore

datastore = DataStore("postgres", "passw0rd", "localhost", 5433, "postgres")

filePath = pathlib.Path(__file__).parent.parent / "Resources/Ambig_tracks2.rep"
rep = REPFile(str(filePath))

with datastore.session_scope() as session:
    datafile = session.addDatafile(rep.getDatafileName(), rep.getDatafileType())
    for repLine in rep.getLines():
        platform = session.addPlatform(repLine.getPlatform())
        sensor = session.addSensor("GPS", platform)
        session.addState(repLine.getTimestamp(), datafile, sensor, repLine.getLatitude(), repLine.getLongitude(), repLine.getHeading(), repLine.getSpeed())
