from PyQt5.QtWidgets import QMainWindow
from gui.main_window_layout import MainWindowLayout
from data_acquisition.accelerator_interface import AcceleratorInterface
from analysis.handle_data import DataAnalyzer
import logging
import sys

# Set up basic logging to print messages to the console
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self, parent=None):
        """Initialize the main window."""
        super(MainWindow, self).__init__(parent)
        
        # Set up the main layout
        self.main_layout = MainWindowLayout(self)
        self.setCentralWidget(self.main_layout)

        # Initialize the application components
        self.initialize()

    def initialize(self):
        """Initialize the application components."""
        # Connect to the accelerator and set up triggers
        self.connect_to_accelerator()
        self.setup_triggers()        
        # Create an instance of the DataAnalyzer
        self.data_analyzer = DataAnalyzer()

    def connect_to_accelerator(self):
        """Connect to the accelerator interface."""
        # Connect to the accelerator interface
        logging.info('Connecting to accelerator.')
        self.accelerator_interface = AcceleratorInterface()
        
        # Connect the data_acquired signal to the handling method
        self.accelerator_interface.data_acquired.connect(self.handle_data_acquired)

    def setup_triggers(self):
        """Set up event triggers for user actions."""
        # Set up event triggers for user actions
        logging.info('Setting up triggers.')
        self.main_layout.retrieve_button.clicked.connect(self.retrieve_data)

    def retrieve_data(self):
        """Retrieve data from the accelerator."""
        # Retrieve data from the accelerator
        logging.info('Retrieving data.')
        self.accelerator_interface.get_data()

    def handle_data_acquired(self, data):
        """Handle the acquired data."""
        # Handle the acquired data (update GUI, perform analysis, etc.)
        logging.info('Handling data...')
        logging.info("Data acquired: %s", data)
        
        # Perform analysis using the DataAnalyzer
        analysis_result = self.data_analyzer.perform_analysis(data)
        logging.info("Analysis Result: %s", analysis_result)
