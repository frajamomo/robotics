from optparse import OptionParser
import logging

def arguments():
    usage = 'usage: %prog [options]'
    description = 'Text describing the purpose of the program.'
    parser = OptionParser(usage = usage, description = description, version = __version__)
    msg =  "Name of the file that contains the heuristic info "
    msg += "of the protocols included in the sigfile. Default: "
    msg += "%s/staging/heuristics_dpi/Package/siginfo.yml" % environ['WS_ROOT']
    parser.add_option("-y", "--yaml-file",
                      dest = "siginfo_yaml",
                      action = "store",
                      default = (environ['WS_ROOT'] + \
                                 '/staging/heuristics_dpi/Package/siginfo.yml'),
                      help = msg)
    parser.add_option("-v", "--verbose",
                      dest = "verbose",
                      action = "store_true",
                      help= "Verbose")

    return parser.parse_args()


def main():

    (options, args) = arguments()

    FORMAT = '[%(asctime)-15s] (heurdefinitions) %(levelname)s: %(message)s'
    logging_level = logging.INFO
    if options.verbose:
        logging_level = logging.DEBUG

    logging.basicConfig(format=FORMAT, level=logging_level)

    errors = call here to your specific code()
    sys.exit(errors)


################################################################################
# Main function
################################################################################
if __name__ == "__main__":
    if sys.version_info < (2, 4):
        print "Python 2.4 or higher required"
        sys.exit(1)

    # Main funtion
    try:
        main()
    except KeyboardInterrupt:
        print "Program interrupted by CTRL-C."
        sys.exit(0)

