__author__ = "Joshua Goldsmith"
__organisation__ = "The Univeristy of Strathclyde"
__support__ = "https://github.com/strath-sdr/rfsoc_frequency_planner"

from .interface import ADCWidgets, DACWidgets, DDCWidgets, DUCWidgets
import ipywidgets as widgets
from pkg_resources import resource_stream

class FrequencyPlannerApplication:
    def __init__(self):
        f = resource_stream('rfsoc_freqplan', 'info.html')
        info = widgets.HTML(value=f.read())
        f.close()

        adc = ADCWidgets().layout
        dac = DACWidgets().layout
        ddc = DDCWidgets().layout
        duc = DUCWidgets().layout

        self.tab = widgets.Tab()
        self.tab.children = [info, adc,dac,ddc,duc]
        self.tab.set_title(0, 'Info')
        self.tab.set_title(1, 'ADC')
        self.tab.set_title(2, 'DAC')
        self.tab.set_title(3, 'DDC')
        self.tab.set_title(4, 'DUC')
