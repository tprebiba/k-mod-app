from data_acquisition.accelerator_interface import AcceleratorInterface

class ModulationAnalyzer:
    def __init__(self, accelerator_interface: AcceleratorInterface):
        # Connect to the data_acquired signal
        accelerator_interface.data_acquired.connect(self.analyze_data)

    def analyze_data(self, data):
        # Implement data analysis based on the acquired data
        print("Analyzing data:", data)