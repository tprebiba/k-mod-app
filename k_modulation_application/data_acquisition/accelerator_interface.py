from PyQt5.QtCore import QObject, pyqtSignal
import numpy as np

class AcceleratorInterface(QObject):
    """Interface for interacting with the accelerator."""

    # Signal emitted when data is acquired
    data_acquired = pyqtSignal(object)

    def connect(self):
        """Connect to the accelerator."""
        # Placeholder method for establishing a connection to the accelerator
        pass

    def start_acquisition(self):
        """Start the data acquisition process."""
        # Placeholder method for starting the data acquisition process
        pass

    def get_data(self):
        """Retrieve data from the accelerator."""
        # Simulate getting data from the accelerator
        data = [0,1,2,3,4,5,6]
        
        # Emit the data_acquired signal with the retrieved data
        self.data_acquired.emit(data)
