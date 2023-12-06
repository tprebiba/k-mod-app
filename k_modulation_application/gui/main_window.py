from PyQt5.QtWidgets import QMainWindow, QAction
from gui.main_window_layout import MainWindowLayout
from data_acquisition.accelerator_interface import AcceleratorInterface
import logging
import sys

# Set up basic logging to print messages to the console
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self, parent=None):
        """Initialize the main window."""
        # Initialize the main window
        logging.info('Initializing main window.')
        super(MainWindow, self).__init__(parent)
        
        # Set up the main layout
        self.main_layout = MainWindowLayout(self)
        self.setCentralWidget(self.main_layout)

        # Initialize the application components
        self.initialize()

    def initialize(self):
        """Initialize the application components."""
        self.connect_to_accelerator()
        self.setup_triggers()        

    def connect_to_accelerator(self):
        """Connect to the accelerator interface."""
        logging.info('Connecting to accelerator.')
        self.accelerator_interface = AcceleratorInterface()
        
        # Connect the data_acquired signal to the handling method
        self.accelerator_interface.data_acquired.connect(self.handle_data_acquired)

    def setup_triggers(self):
        """Set up event triggers for user actions."""
        logging.info('Setting up triggers.')
        
        # Option 1: Using QAction (commented out)
        # retrieve_action = QAction("Retrieve Data", self)
        # retrieve_action.triggered.connect(self.retrieve_data)
        # self.main_layout.retrieve_button.addAction(retrieve_action)

        # Option 2: Directly connecting to clicked signal
        self.main_layout.retrieve_button.clicked.connect(self.retrieve_data)

    def retrieve_data(self):
        """Retrieve data from the accelerator."""
        logging.info('Retrieving data.')
        self.accelerator_interface.get_data()

    def handle_data_acquired(self, data):
        """Handle the acquired data."""
        # Handle the acquired data (update GUI, perform analysis, etc.)
        logging.info('Handling data...')
        logging.info("Data acquired: %s", data)
