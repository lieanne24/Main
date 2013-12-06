from flask import Flask
from flaskext.markdown import Markdown  # @UnresolvedImport

##
##CODE TO INITIALIZE THE DATABASE CONNECTION BEGINS HERE
##

import MySQLdb
import ConfigParser
import sys

# First, read in the config file for database connection parameters and exit on failure
try:
    db_config = ConfigParser.ConfigParser()
    db_config.read("database.ini")
except:
    sys.exit("Failed to read configuration file")  # @UndefinedVariable
    

# ConfigMapper creates a dictionary of the options from a given section of the config file
# If any option generates an exception, then set that option to an empty string
def ConfigMapper(config_section):
    conf_dict = {}
    options = db_config.options(config_section)
    for opt in options:
            try:
                    conf_dict[opt] = db_config.get(config_section, opt)
            except:
                    print("Exception on %s!" % opt)
                    conf_dict[opt] = ""
    return conf_dict

# Get a dictionary of the Database section of the config file (currently the only section)
db_options = ConfigMapper("Database")

# Try connecting to the database with the given information
try:
    cnx = MySQLdb.connect(
                                host= db_options["host"],
                                port= int(db_options["port"]),  # @UndefinedVariable
                                user= db_options["user"],
                                passwd= db_options["pass"],
                                db= db_options["schema"])
except:
    sys.exit("Failed to connect to database")  # @UndefinedVariable

##
##CODE TO INITIALIZE THE DATABASE CONNECTION ENDS HERE
##

app = Flask(__name__)
app.secret_key = 'development key'

Markdown(app)