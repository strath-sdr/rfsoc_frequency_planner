from fp_widgets import ADCWidgets, DACWidgets, DDCWidgets, DUCWidgets
import ipywidgets as widgets

class FrequencyPlannerApp:
    def __init__(self):
        adc = ADCWidgets().layout
        dac = DACWidgets().layout
        ddc = DDCWidgets().layout
        duc = DUCWidgets().layout

        self.tab = widgets.Tab()
        self.tab.children = [adc,dac,ddc,duc]
        self.tab.set_title(0, 'ADC')
        self.tab.set_title(1, 'DAC')
        self.tab.set_title(2, 'DDC')
        self.tab.set_title(3, 'DUC')
