from ipywidgets import widgets
import plotly.graph_objs as go
from frequency_calc import FrequencyPlannerADC, FrequencyPlannerDAC, FrequencyPlannerDDC, FrequencyPlannerDUC

class ADCWidgets:
    def __init__(self):
        self.data = FrequencyPlannerADC()
        
        self._plot = self.__setup_plot()
        
        self._label_layout = widgets.Layout(width='80px')
        self._slider_layout = widgets.Layout(width='120px')
        self._entry_layout = widgets.Layout(width='90px')
        self._units_layout = widgets.Layout(width='37px')
        self._button_layout = widgets.Layout(width='87px', fontsize=12)
        
        self.fs_label  = widgets.Label("Fs", layout=self._label_layout)
        self.fs_slider = widgets.FloatSlider(value=self.data.fs_rf, min=1000.0, max=5000, step=0.01, readout=False, layout=self._slider_layout)
        self.fs_entry  = widgets.BoundedFloatText(value=self.fs_slider.value, min=self.fs_slider.min, max=self.fs_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.fs_units  = widgets.Label("MSPS", layout=self._units_layout)
        widgets.jslink((self.fs_slider, 'value'), (self.fs_entry, 'value'))
        self.fs_slider.observe(self.__update_fs, 'value')
        
        self.fc_label  = widgets.Label("Fc", layout=self._label_layout)
        self.fc_slider = widgets.FloatSlider(value=self.data.fc, min=0, max=6000, step=0.01, readout=False, layout=self._slider_layout)
        self.fc_entry  = widgets.BoundedFloatText(value=self.fc_slider.value, min=self.fc_slider.min, max=self.fc_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.fc_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.fc_slider, 'value'), (self.fc_entry, 'value'))
        self.fc_slider.observe(self.__update_fc, 'value')
        
        self.bw_label  = widgets.Label("Bandwidth", layout=self._label_layout)
        self.bw_slider = widgets.FloatSlider(value=self.data.fs_bw, min=0.0, max=500.0, step=0.01, readout=False, layout=self._slider_layout)
        self.bw_entry  = widgets.BoundedFloatText(value=self.bw_slider.value, min=self.bw_slider.min, max=self.bw_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.bw_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.bw_slider, 'value'), (self.bw_entry, 'value'))
        self.bw_slider.observe(self.__update_bw, 'value')
        
        self.pll_label  = widgets.Label("PLL Ref Clk", layout=self._label_layout)
        self.pll_slider = widgets.FloatSlider(value=self.data.pll_ref, min=102.5, max=614.0, step=0.01, readout=False, layout=self._slider_layout)
        self.pll_entry  = widgets.BoundedFloatText(value=self.pll_slider.value, min=self.pll_slider.min, max=self.pll_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.pll_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.pll_slider, 'value'), (self.pll_entry, 'value'))
        self.pll_slider.observe(self.__update_pll, 'value')
        
        self.il_label  = widgets.Label("IL Factor", layout=self._label_layout)
        self.il_blank = widgets.Label("", layout=self._slider_layout)
        self.il_entry  = widgets.Dropdown(options=["4","8"],value="8", layout=self._entry_layout)
        self.il_units  = widgets.Label("X", layout=self._units_layout)
        self.il_entry.observe(self.__update_il, 'value')
        
        self.calibration = widgets.Label(self.data.calibration_mode, layout=widgets.Layout(flex='auto'))

        
        self.param_controls = widgets.Accordion([widgets.VBox([
            widgets.HBox([self.fs_label, self.fs_slider, self.fs_entry, self.fs_units]),
            widgets.HBox([self.fc_label, self.fc_slider, self.fc_entry, self.fc_units]),
            widgets.HBox([self.bw_label, self.bw_slider, self.bw_entry, self.bw_units]),
            widgets.HBox([self.pll_label, self.pll_slider, self.pll_entry, self.pll_units]),
            widgets.HBox([self.il_label, self.il_blank, self.il_entry, self.il_units])])
        ])
        self.param_controls.set_title(0, 'RF-DC Parameters')

        self.params = widgets.VBox([
            self.param_controls,
            widgets.HBox([self.calibration])
            ])
        
        self.layout = widgets.HBox([self.params, self._plot])
        
    def __update_fs(self, change):
        self.data.fs_rf = change['new']
        self.__update_plot()
        
    def __update_fc(self, change):
        self.data.fc = change['new']
        self.__update_plot()
        
    def __update_bw(self, change):
        self.data.fs_bw = change['new']
        self.__update_plot()
        
    def __update_pll(self, change):
        self.data.pll_ref = change['new']
        self.__update_plot()
        
    def __update_il(self, change):
        self.data.il_factor = int(change['new'])
        self.__update_plot()
    
    def __update_plot(self):
        spurs_list = [self.data.hd2, self.data.hd3, self.data.hd4, self.data.hd5,
                     self.data.il_rx1, self.data.il_rx2, self.data.il_rx3, self.data.il_rx4, self.data.il_rx5,
                     self.data.fs8_p_hd3, self.data.fs8_m_hd3, self.data.fs8_p_hd2, self.data.fs8_m_hd2, self.data.fs4_p_hd3, self.data.fs4_m_hd3, self.data.fs4_p_hd2, self.data.fs4_m_hd2, self.data.fs2_m_hd3, self.data.fs2_m_hd2,
                     self.data.pll_mix_up, self.data.pll_mix_down]
        
        
        with self._plot.batch_update():
            self._plot.data[0].x = [self.data.rx_band['xmin'], self.data.rx_band['xmax']]
            self._plot.data[1].x = [self.data.rx_band['xmin'], self.data.rx_band['xmin']]
            self._plot.data[2].x = [self.data.rx_band['xmax'], self.data.rx_band['xmax']]
            
            self._plot.data[3].x = [self.data.nyquist['xmax'], self.data.nyquist['xmax']]
            
            for i in range(len(spurs_list)):
                if (spurs_list[i]['xmin'] != 0) and (spurs_list[i]['xmax'] != 0):
                    self._plot.data[i+4].x = [spurs_list[i]['xmin'], spurs_list[i]['xmax']]
                    self._plot.data[i+4].visible = True
                    
                    if self.__intersection(spurs_list[i], self.data.rx_band):
                        self._plot.data[i+4].line['color'] = 'red'
                    else:
                        self._plot.data[i+4].line['color'] = spurs_list[i]['color']
                else:
                    self._plot.data[i+4].visible = False
                
        self.calibration.value = self.data.calibration_mode
    
    def __setup_plot(self):
        rx_band = go.Scatter(x=[self.data.rx_band['xmin'], self.data.rx_band['xmax']], y=[self.data.rx_band['ymax'], self.data.rx_band['ymax']], line=dict(color=self.data.rx_band['color']), name=self.data.rx_band['label'], legendgroup="rx", hovertext=self.data.rx_band['label'], hoverinfo='text+x')
        rx_band_l = go.Scatter(x=[self.data.rx_band['xmin'], self.data.rx_band['xmin']], y=[self.data.rx_band['ymin'], self.data.rx_band['ymax']], line=dict(color=self.data.rx_band['color']), name=self.data.rx_band['label'], showlegend=False, legendgroup="rx", hovertext=self.data.rx_band['label'], hoverinfo='text+x')
        rx_band_r = go.Scatter(x=[self.data.rx_band['xmax'], self.data.rx_band['xmax']], y=[self.data.rx_band['ymin'], self.data.rx_band['ymax']], line=dict(color=self.data.rx_band['color']), name=self.data.rx_band['label'], showlegend=False, legendgroup="rx", hovertext=self.data.rx_band['label'], hoverinfo='text+x')
        nyq = go.Scatter(x=[self.data.nyquist['xmin'], self.data.nyquist['xmin']], y=[self.data.nyquist['ymin'], self.data.nyquist['ymax']], line=dict(color=self.data.rx_band['color']), name=self.data.nyquist['label'], hovertext=self.data.nyquist['label'], hoverinfo='text+x')

        spurs_list = [self.data.hd2, self.data.hd3, self.data.hd4, self.data.hd5,
                     self.data.il_rx1, self.data.il_rx2, self.data.il_rx3, self.data.il_rx4, self.data.il_rx5,
                     self.data.fs8_p_hd3, self.data.fs8_m_hd3, self.data.fs8_p_hd2, self.data.fs8_m_hd2, self.data.fs4_p_hd3, self.data.fs4_m_hd3, self.data.fs4_p_hd2, self.data.fs4_m_hd2, self.data.fs2_m_hd3, self.data.fs2_m_hd2,
                     self.data.pll_mix_up, self.data.pll_mix_down]
        
        spurs = [go.Scatter(x=[d['xmin'], d['xmax']], y=[d['ymax'], d['ymax']], name=d['label'], hovertext=d['label'], hoverinfo='text+x', line=dict(color=d['color'])) for d in spurs_list]
        
        plot_items = [rx_band, rx_band_l, rx_band_r, nyq] + spurs
        plot = go.FigureWidget(plot_items)
        
        plot.update_layout(
            title={'text':"Digital Receiver Frequency Plan", 'x':0.5, 'y':0.9, 'xanchor':'center', 'yanchor':'top'},
            xaxis_title={'text':"Frequency (MHz)"},
            yaxis_title={'text':"Harmonic No."},
            width=900,
            height=500,
        )
        
        return plot
    
    def __intersection(self, a, b):
        if ((a['xmin'] < b['xmax']) and (a['xmax'] < b['xmin'])) or ((a['xmin'] > b['xmax']) and (a['xmax'] > b['xmin'])):
            return False
        else:
            return True

class DACWidgets:
    def __init__(self):
        self.data = FrequencyPlannerDAC() 
        self._plot = self.__setup_plot()
        
        self._label_layout = widgets.Layout(width='80px')
        self._slider_layout = widgets.Layout(width='120px')
        self._entry_layout = widgets.Layout(width='90px')
        self._units_layout = widgets.Layout(width='37px')
        self._button_layout = widgets.Layout(width='87px', fontsize=12)
        
        self.fs_label  = widgets.Label("Fs", layout=self._label_layout)
        self.fs_slider = widgets.FloatSlider(value=self.data.fs_rf, min=1000.0, max=5000, step=0.01, readout=False, layout=self._slider_layout)
        self.fs_entry  = widgets.BoundedFloatText(value=self.fs_slider.value, min=self.fs_slider.min, max=self.fs_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.fs_units  = widgets.Label("MSPS", layout=self._units_layout)
        widgets.jslink((self.fs_slider, 'value'), (self.fs_entry, 'value'))
        self.fs_slider.observe(self.__update_fs, 'value')

        self.fc_label  = widgets.Label("Fc", layout=self._label_layout)
        self.fc_slider = widgets.FloatSlider(value=self.data.fc, min=0, max=6000, step=0.01, readout=False, layout=self._slider_layout)
        self.fc_entry  = widgets.BoundedFloatText(value=self.fc_slider.value, min=self.fc_slider.min, max=self.fc_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.fc_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.fc_slider, 'value'), (self.fc_entry, 'value'))
        self.fc_slider.observe(self.__update_fc, 'value')
        
        self.bw_label  = widgets.Label("Bandwidth", layout=self._label_layout)
        self.bw_slider = widgets.FloatSlider(value=self.data.fs_bw, min=0.0, max=500.0, step=0.01, readout=False, layout=self._slider_layout)
        self.bw_entry  = widgets.BoundedFloatText(value=self.bw_slider.value, min=self.bw_slider.min, max=self.bw_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.bw_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.bw_slider, 'value'), (self.bw_entry, 'value'))
        self.bw_slider.observe(self.__update_bw, 'value')
        
        self.pll_label  = widgets.Label("PLL Ref Clk", layout=self._label_layout)
        self.pll_slider = widgets.FloatSlider(value=self.data.pll_ref, min=102.5, max=614.0, step=0.01, readout=False, layout=self._slider_layout)
        self.pll_entry  = widgets.BoundedFloatText(value=self.pll_slider.value, min=self.pll_slider.min, max=self.pll_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.pll_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.pll_slider, 'value'), (self.pll_entry, 'value'))
        self.pll_slider.observe(self.__update_pll, 'value')

        self.mix_mode = widgets.Label(self.data.mix_mode, layout=widgets.Layout(flex='auto'))

        self.param_controls = widgets.Accordion([widgets.VBox([
            widgets.HBox([self.fs_label, self.fs_slider, self.fs_entry, self.fs_units]),
            widgets.HBox([self.fc_label, self.fc_slider, self.fc_entry, self.fc_units]),
            widgets.HBox([self.bw_label, self.bw_slider, self.bw_entry, self.bw_units]),
            widgets.HBox([self.pll_label, self.pll_slider, self.pll_entry, self.pll_units])])
        ])
        self.param_controls.set_title(0,"RF-DC Parameters")

        self.params = widgets.VBox([self.param_controls, self.mix_mode])
        
        self.layout = widgets.HBox([self.params, self._plot])
        
    def __update_fs(self, change):
        self.data.fs_rf = change['new']
        self.__update_plot()
        
    def __update_fc(self, change):
        self.data.fc = change['new']
        self.__update_plot()
        
    def __update_bw(self, change):
        self.data.fs_bw = change['new']
        self.__update_plot()
        
    def __update_pll(self, change):
        self.data.pll_ref = change['new']
        self.__update_plot()
        
    def __update_plot(self):
        spurs_list = [self.data.hd2_nyq1,self.data.hd3_nyq1,self.data.hd4_nyq1,self.data.hd5_nyq1,
                      self.data.hd2_nyq2,self.data.hd3_nyq2,self.data.hd4_nyq2,self.data.hd5_nyq2,
                      self.data.pll_mix_up,self.data.pll_mix_up_image,
                      self.data.pll_mix_down,self.data.pll_mix_down_image]
        
        
        with self._plot.batch_update():
            self._plot.data[0].x = [self.data.tx_band['xmin'], self.data.tx_band['xmax']]
            self._plot.data[1].x = [self.data.tx_band['xmin'], self.data.tx_band['xmin']]
            self._plot.data[2].x = [self.data.tx_band['xmax'], self.data.tx_band['xmax']]
            
            self._plot.data[3].x = [self.data.fimg['xmin'], self.data.fimg['xmax']]
            self._plot.data[4].x = [self.data.fimg['xmin'], self.data.fimg['xmin']]
            self._plot.data[5].x = [self.data.fimg['xmax'], self.data.fimg['xmax']]
            
            self._plot.data[6].x = [self.data.nyquist['xmax'], self.data.nyquist['xmax']]
            self._plot.data[7].x = [self.data.nyquist_image['xmax'], self.data.nyquist_image['xmax']]
            
            for i in range(len(spurs_list)):
                self._plot.data[i+8].x = [spurs_list[i]['xmin'], spurs_list[i]['xmax']]
                
        self.mix_mode.value = self.data.mix_mode
            
    def __setup_plot(self):
        tx_band = go.Scatter(x=[self.data.tx_band['xmin'], self.data.tx_band['xmax']], y=[self.data.tx_band['ymax'], self.data.tx_band['ymax']], line=dict(color='red'), name=self.data.tx_band['label'], legendgroup="tx", hovertext=self.data.tx_band['label'], hoverinfo='text+x')
        tx_band_l = go.Scatter(x=[self.data.tx_band['xmin'], self.data.tx_band['xmin']], y=[self.data.tx_band['ymin'], self.data.tx_band['ymax']], line=dict(color='red'), name=self.data.tx_band['label'], showlegend=False, legendgroup="tx", hovertext=self.data.tx_band['label'], hoverinfo='text+x')
        tx_band_r = go.Scatter(x=[self.data.tx_band['xmax'], self.data.tx_band['xmax']], y=[self.data.tx_band['ymin'], self.data.tx_band['ymax']], line=dict(color='red'), name=self.data.tx_band['label'], showlegend=False, legendgroup="tx", hovertext=self.data.tx_band['label'], hoverinfo='text+x')

        fimag = go.Scatter(x=[self.data.fimg['xmin'], self.data.fimg['xmax']], y=[self.data.fimg['ymax'], self.data.fimg['ymax']], line=dict(color='blue'), name=self.data.fimg['label'], legendgroup="fimg", hovertext=self.data.fimg['label'], hoverinfo='text+x')
        fimag_l = go.Scatter(x=[self.data.fimg['xmin'], self.data.fimg['xmin']], y=[self.data.fimg['ymin'], self.data.fimg['ymax']], line=dict(color='blue'), name=self.data.fimg['label'], showlegend=False, legendgroup="fimg", hovertext=self.data.fimg['label'], hoverinfo='text+x')
        fimag_r = go.Scatter(x=[self.data.fimg['xmax'], self.data.fimg['xmax']], y=[self.data.fimg['ymin'], self.data.fimg['ymax']], line=dict(color='blue'), name=self.data.fimg['label'], showlegend=False, legendgroup="fimg", hovertext=self.data.fimg['label'], hoverinfo='text+x')

        nyq = go.Scatter(x=[self.data.nyquist['xmin'], self.data.nyquist['xmin']], y=[self.data.nyquist['ymin'], self.data.nyquist['ymax']], line=dict(color='grey'), name=self.data.nyquist['label'], hovertext=self.data.nyquist['label'], hoverinfo='text+x')
        nyq_img = go.Scatter(x=[self.data.nyquist_image['xmin'], self.data.nyquist_image['xmin']], y=[self.data.nyquist_image['ymin'], self.data.nyquist_image['ymax']], line=dict(color='green'), name=self.data.nyquist_image['label'], hovertext=self.data.nyquist_image['label'], hoverinfo='text+x')
        
        spurs_list = [self.data.hd2_nyq1,self.data.hd3_nyq1,self.data.hd4_nyq1,self.data.hd5_nyq1,
                      self.data.hd2_nyq2,self.data.hd3_nyq2,self.data.hd4_nyq2,self.data.hd5_nyq2,
                      self.data.pll_mix_up,self.data.pll_mix_up_image,
                      self.data.pll_mix_down,self.data.pll_mix_down_image]

        spurs = [go.Scatter(x=[d['xmin'], d['xmax']], y=[d['ymax'], d['ymax']], name=d['label'], hovertext=d['label'], hoverinfo='text+x') for d in spurs_list]
        
        plot_items = [tx_band, tx_band_l, tx_band_r, fimag, fimag_l, fimag_r, nyq, nyq_img] + spurs
        plot = go.FigureWidget(plot_items)
        
        plot.update_layout(
            title={'text':"Digital Transmitter Frequency Plan", 'x':0.5, 'y':0.9, 'xanchor':'center', 'yanchor':'top'},
            xaxis_title={'text':"Frequency (MHz)"},
            yaxis_title={'text':"Harmonic No."},
            width=900,
            height=500
        )

        return plot

class DDCWidgets:
    def __init__(self):
        self.data = FrequencyPlannerDDC()
        self._plot = self.__setup_plot()
        
        self._label_layout = widgets.Layout(width='90px')
        self._slider_layout = widgets.Layout(width='120px')
        self._entry_layout = widgets.Layout(width='90px')
        self._units_layout = widgets.Layout(width='55px')
        self._button_layout = widgets.Layout(width='87px', fontsize=12)
        
        self.fs_label  = widgets.Label("Fs", layout=self._label_layout)
        self.fs_slider = widgets.FloatSlider(value=self.data.fs_rf, min=1000.0, max=5000, step=0.01, readout=False, layout=self._slider_layout)
        self.fs_entry  = widgets.BoundedFloatText(value=self.fs_slider.value, min=self.fs_slider.min, max=self.fs_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.fs_units  = widgets.Label("MSPS", layout=self._units_layout)
        widgets.jslink((self.fs_slider, 'value'), (self.fs_entry, 'value'))
        self.fs_slider.observe(self.__update_fs, 'value')
        
        self.fc_label  = widgets.Label("Fc", layout=self._label_layout)
        self.fc_slider = widgets.FloatSlider(value=self.data.fc, min=0, max=6000, step=0.01, readout=False, layout=self._slider_layout)
        self.fc_entry  = widgets.BoundedFloatText(value=self.fc_slider.value, min=self.fc_slider.min, max=self.fc_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.fc_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.fc_slider, 'value'), (self.fc_entry, 'value'))
        self.fc_slider.observe(self.__update_fc, 'value')
        
        self.pll_label  = widgets.Label("PLL Ref Clk", layout=self._label_layout)
        self.pll_slider = widgets.FloatSlider(value=self.data.pll_ref, min=102.5, max=614.0, step=0.01, readout=False, layout=self._slider_layout)
        self.pll_entry  = widgets.BoundedFloatText(value=self.pll_slider.value, min=self.pll_slider.min, max=self.pll_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.pll_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.pll_slider, 'value'), (self.pll_entry, 'value'))
        self.pll_slider.observe(self.__update_pll, 'value')
        
        self.dec_label  = widgets.Label("Decimation", layout=self._label_layout)
        self.dec_blank = widgets.Label("", layout=self._slider_layout)
        self.dec_entry  = widgets.Dropdown(options=["1", "2","4","8"],value="1", layout=self._entry_layout)
        self.dec_units  = widgets.Label("X", layout=self._units_layout)
        self.dec_entry.observe(self.__update_dec, 'value')
        
        self.il_label  = widgets.Label("IL Factor", layout=self._label_layout)
        self.il_blank = widgets.Label("", layout=self._slider_layout)
        self.il_entry  = widgets.Dropdown(options=["4","8"],value="8", layout=self._entry_layout)
        self.il_units  = widgets.Label("X", layout=self._units_layout)
        self.il_entry.observe(self.__update_il, 'value')
        
        self.nco_label  = widgets.Label("NCO", layout=self._label_layout)
        self.nco_slider = widgets.FloatSlider(value=self.data.nco, min=0, max=4096, step=0.01, readout=False, layout=self._slider_layout)
        self.nco_entry  = widgets.BoundedFloatText(value=self.nco_slider.value, min=self.nco_slider.min, max=self.nco_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.nco_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.nco_slider, 'value'), (self.nco_entry, 'value'))
        self.nco_slider.observe(self.__update_nco, 'value')
        
        self.hd2_label  = widgets.Label("HD2", layout=self._label_layout)
        self.hd2_slider = widgets.FloatSlider(value=self.data.hd2_db, min=0, max=200, step=0.01, readout=False, layout=self._slider_layout)
        self.hd2_entry  = widgets.BoundedFloatText(value=self.hd2_slider.value, min=self.hd2_slider.min, max=self.hd2_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.hd2_units  = widgets.Label("dB", layout=self._units_layout)
        widgets.jslink((self.hd2_slider, 'value'), (self.hd2_entry, 'value'))
        self.hd2_slider.observe(self.__update_hd2, 'value')
        
        self.hd3_label  = widgets.Label("HD3", layout=self._label_layout)
        self.hd3_slider = widgets.FloatSlider(value=self.data.hd3_db, min=0, max=200, step=0.01, readout=False, layout=self._slider_layout)
        self.hd3_entry  = widgets.BoundedFloatText(value=self.hd3_slider.value, min=self.hd3_slider.min, max=self.hd3_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.hd3_units  = widgets.Label("dB", layout=self._units_layout)
        widgets.jslink((self.hd3_slider, 'value'), (self.hd3_entry, 'value'))
        self.hd3_slider.observe(self.__update_hd3, 'value')
        
        self.tis_label  = widgets.Label("TI Spur", layout=self._label_layout)
        self.tis_slider = widgets.FloatSlider(value=self.data.tis_spur_db, min=0, max=200, step=0.01, readout=False, layout=self._slider_layout)
        self.tis_entry  = widgets.BoundedFloatText(value=self.tis_slider.value, min=self.tis_slider.min, max=self.tis_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.tis_units  = widgets.Label("dB", layout=self._units_layout)
        widgets.jslink((self.tis_slider, 'value'), (self.tis_entry, 'value'))
        self.tis_slider.observe(self.__update_tis, 'value')
        
        self.oss_label  = widgets.Label("Offset Spur", layout=self._label_layout)
        self.oss_slider = widgets.FloatSlider(value=self.data.off_spur_db, min=0, max=200, step=0.01, readout=False, layout=self._slider_layout)
        self.oss_entry  = widgets.BoundedFloatText(value=self.oss_slider.value, min=self.oss_slider.min, max=self.oss_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.oss_units  = widgets.Label("dB", layout=self._units_layout)
        widgets.jslink((self.oss_slider, 'value'), (self.oss_entry, 'value'))
        self.oss_slider.observe(self.__update_oss, 'value')
        
        self.pdb_label  = widgets.Label("PLL Ref Mixing", layout=self._label_layout)
        self.pdb_slider = widgets.FloatSlider(value=self.data.pll_mix_db, min=0, max=200, step=0.01, readout=False, layout=self._slider_layout)
        self.pdb_entry  = widgets.BoundedFloatText(value=self.pdb_slider.value, min=self.pdb_slider.min, max=self.pdb_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.pdb_units  = widgets.Label("dB", layout=self._units_layout)
        widgets.jslink((self.pdb_slider, 'value'), (self.pdb_entry, 'value'))
        self.pdb_slider.observe(self.__update_pdb, 'value')
        
        self.nsd_label  = widgets.Label("NSD", layout=self._label_layout)
        self.nsd_slider = widgets.FloatSlider(value=self.data.nsd_db, min=-300, max=0, step=0.01, readout=False, layout=self._slider_layout)
        self.nsd_entry  = widgets.BoundedFloatText(value=self.nsd_slider.value, min=self.nsd_slider.min, max=self.nsd_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.nsd_units  = widgets.Label("dBFs/Hz", layout=self._units_layout)
        widgets.jslink((self.nsd_slider, 'value'), (self.nsd_entry, 'value'))
        self.nsd_slider.observe(self.__update_nsd, 'value')
        
        self.param_controls = widgets.Accordion([widgets.VBox([
            widgets.HBox([self.fs_label, self.fs_slider, self.fs_entry, self.fs_units]),
            widgets.HBox([self.fc_label, self.fc_slider, self.fc_entry, self.fc_units]),
            widgets.HBox([self.pll_label, self.pll_slider, self.pll_entry, self.pll_units]),
            widgets.HBox([self.nco_label, self.nco_slider, self.nco_entry, self.nco_units]),
            widgets.HBox([self.dec_label, self.dec_blank, self.dec_entry, self.dec_units]),
            widgets.HBox([self.il_label, self.il_blank, self.il_entry, self.il_units])])
        ])
        self.param_controls.set_title(0,"RF-DC Parameters")

        self.amp_controls = widgets.Accordion([widgets.VBox([
            widgets.HBox([self.hd2_label, self.hd2_slider, self.hd2_entry, self.hd2_units]),
            widgets.HBox([self.hd3_label, self.hd3_slider, self.hd3_entry, self.hd3_units]),
            widgets.HBox([self.tis_label, self.tis_slider, self.tis_entry, self.tis_units]),
            widgets.HBox([self.oss_label, self.oss_slider, self.oss_entry, self.oss_units]),
            widgets.HBox([self.pdb_label, self.pdb_slider, self.pdb_entry, self.pdb_units]),
            widgets.HBox([self.nsd_label, self.nsd_slider, self.nsd_entry, self.nsd_units])])
        ])
        self.amp_controls.set_title(0,"Spur Amplitude")

        self.params = widgets.VBox([self.param_controls, self.amp_controls])

        
        self.layout = widgets.HBox([self.params, self._plot])
        
    def __update_fs(self, change):
        self.data.fs_rf = change['new']
        self.__update_plot()
            
    def __update_fc(self, change):
        self.data.fc = change['new']
        self.__update_plot()
        
    def __update_dec(self, change):
        self.data.dec = int(change['new'])
        self.__update_plot()
        
    def __update_il(self, change):
        self.data.il_factor = int(change['new'])
        self.__update_plot()
        
    def __update_pll(self, change):
        self.data.pll_ref = change['new']
        self.__update_plot()
        
    def __update_nco(self, change):
        self.data.nco = change['new']
        self.__update_plot()
        
    def __update_hd2(self, change):
        self.data.hd2_db = change['new']
        self.__update_plot()
        
    def __update_hd3(self, change):
        self.data.hd3_db = change['new']
        self.__update_plot()
        
    def __update_tis(self, change):
        self.data.tis_spur_db = change['new']
        self.__update_plot()
        
    def __update_oss(self, change):
        self.data.off_spur_db = change['new']
        self.__update_plot()
        
    def __update_pdb(self, change):
        self.data.pll_mix_db = change['new']
        self.__update_plot()
        
    def __update_nsd(self, change):
        self.data.nsd_db = change['new']
        self.__update_plot()
        
    def __setup_plot(self):      
        spurs_list = [self.data.nyquist_up, self.data.nyquist_down, self.data.hd2, self.data.hd2_image, 
                     self.data.hd3, self.data.hd3_image, self.data.pll_mix_up, self.data.pll_mix_up_image,
                     self.data.pll_mix_down, self.data.pll_mix_down_image, self.data.rx_image, self.data.rx_alias,
                    self.data.tis_spur, self.data.tis_spur_image, self.data.offset_spur, self.data.offset_spur_image]

        plot_items = [go.Scatter(x=[d['x'], d['x']], y=[d['ymin'], d['ymax']], name=d['label'], hovertext=d['label'], hoverinfo='text+x') for d in spurs_list]

        plot = go.FigureWidget(plot_items)
        
        plot.update_layout(
            title={'text':"Digital Down Converter (DDC)", 'x':0.5, 'y':0.9, 'xanchor':'center', 'yanchor':'top'},
            xaxis_title={'text':"Frequency (MHz)"},
            yaxis_title={'text':"Amplitude (dB)"},
            width=900,
            height=500
        )
        
        plot.add_hline(y=0, line=dict(color='grey'))
        
        return plot
    
    def __update_plot(self):
        spurs_list = [self.data.nyquist_up, self.data.nyquist_down, self.data.hd2, self.data.hd2_image, 
                     self.data.hd3, self.data.hd3_image, self.data.pll_mix_up, self.data.pll_mix_up_image,
                     self.data.pll_mix_down, self.data.pll_mix_down_image, self.data.rx_image, self.data.rx_alias,
                    self.data.tis_spur, self.data.tis_spur_image, self.data.offset_spur, self.data.offset_spur_image]
        
        with self._plot.batch_update():
            for i in range(len(spurs_list)):
                self._plot.data[i].x = [spurs_list[i]['x'], spurs_list[i]['x']]
                self._plot.data[i].y = [spurs_list[i]['ymin'], spurs_list[i]['ymax']]

class DUCWidgets:
    def __init__(self):
        self.data = FrequencyPlannerDUC()
        self._plot = self.__setup_plot()
        
        self._label_layout = widgets.Layout(width='90px')
        self._slider_layout = widgets.Layout(width='120px')
        self._entry_layout = widgets.Layout(width='90px')
        self._units_layout = widgets.Layout(width='37px')
        self._button_layout = widgets.Layout(width='87px', fontsize=12)
        
        self.fs_label  = widgets.Label("Fs", layout=self._label_layout)
        self.fs_slider = widgets.FloatSlider(value=self.data.fs_rf, min=1000.0, max=5000, step=0.01, readout=False, layout=self._slider_layout)
        self.fs_entry  = widgets.BoundedFloatText(value=self.fs_slider.value, min=self.fs_slider.min, max=self.fs_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.fs_units  = widgets.Label("MSPS", layout=self._units_layout)
        widgets.jslink((self.fs_slider, 'value'), (self.fs_entry, 'value'))
        self.fs_slider.observe(self.__update_fs, 'value')
        
        self.fc_label  = widgets.Label("Fc", layout=self._label_layout)
        self.fc_slider = widgets.FloatSlider(value=self.data.fc, min=0, max=6000, step=0.01, readout=False, layout=self._slider_layout)
        self.fc_entry  = widgets.BoundedFloatText(value=self.fc_slider.value, min=self.fc_slider.min, max=self.fc_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.fc_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.fc_slider, 'value'), (self.fc_entry, 'value'))
        self.fc_slider.observe(self.__update_fc, 'value')
        
        self.nco_label  = widgets.Label("NCO", layout=self._label_layout)
        self.nco_slider = widgets.FloatSlider(value=self.data.nco, min=0, max=4096, step=0.01, readout=False, layout=self._slider_layout)
        self.nco_entry  = widgets.BoundedFloatText(value=self.nco_slider.value, min=self.nco_slider.min, max=self.nco_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.nco_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.nco_slider, 'value'), (self.nco_entry, 'value'))
        self.nco_slider.observe(self.__update_nco, 'value') 
        
        self.pll_label  = widgets.Label("PLL Ref Clk", layout=self._label_layout)
        self.pll_slider = widgets.FloatSlider(value=self.data.pll_ref, min=102.5, max=614.0, step=0.01, readout=False, layout=self._slider_layout)
        self.pll_entry  = widgets.BoundedFloatText(value=self.pll_slider.value, min=self.pll_slider.min, max=self.pll_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.pll_units  = widgets.Label("MHz", layout=self._units_layout)
        widgets.jslink((self.pll_slider, 'value'), (self.pll_entry, 'value'))
        self.pll_slider.observe(self.__update_pll, 'value')
        
        self.itrp_label  = widgets.Label("Interpolation", layout=self._label_layout)
        self.itrp_blank = widgets.Label("", layout=self._slider_layout)
        self.itrp_entry  = widgets.Dropdown(options=["1", "2","4","8"],value="1", layout=self._entry_layout)
        self.itrp_units  = widgets.Label("X", layout=self._units_layout)
        self.itrp_entry.observe(self.__update_itrp, 'value')
        
        self.sinc_label  = widgets.Label("Inverse Sinc", layout=self._label_layout)
        self.sinc_blank = widgets.Label("", layout=self._slider_layout)
        self.sinc_entry  = widgets.Dropdown(options=["ON", "OFF"],value="ON", layout=self._entry_layout)
        self.sinc_units  = widgets.Label("X", layout=self._units_layout)
        self.sinc_entry.observe(self.__update_sinc, 'value')
        
        self.hd2_label  = widgets.Label("HD2", layout=self._label_layout)
        self.hd2_slider = widgets.FloatSlider(value=self.data.hd2_db, min=0, max=200, step=0.01, readout=False, layout=self._slider_layout)
        self.hd2_entry  = widgets.BoundedFloatText(value=self.hd2_slider.value, min=self.hd2_slider.min, max=self.hd2_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.hd2_units  = widgets.Label("dB", layout=self._units_layout)
        widgets.jslink((self.hd2_slider, 'value'), (self.hd2_entry, 'value'))
        self.hd2_slider.observe(self.__update_hd2, 'value')
        
        self.hd3_label  = widgets.Label("HD3", layout=self._label_layout)
        self.hd3_slider = widgets.FloatSlider(value=self.data.hd3_db, min=0, max=200, step=0.01, readout=False, layout=self._slider_layout)
        self.hd3_entry  = widgets.BoundedFloatText(value=self.hd3_slider.value, min=self.hd3_slider.min, max=self.hd3_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.hd3_units  = widgets.Label("dB", layout=self._units_layout)
        widgets.jslink((self.hd3_slider, 'value'), (self.hd3_entry, 'value'))
        self.hd3_slider.observe(self.__update_hd3, 'value')
        
        self.pdb_label  = widgets.Label("PLL Ref Mixing", layout=self._label_layout)
        self.pdb_slider = widgets.FloatSlider(value=self.data.pll_db, min=0, max=200, step=0.01, readout=False, layout=self._slider_layout)
        self.pdb_entry  = widgets.BoundedFloatText(value=self.pdb_slider.value, min=self.pdb_slider.min, max=self.pdb_slider.max, step=0.01, continuous_update=False, layout=self._entry_layout)
        self.pdb_units  = widgets.Label("dB", layout=self._units_layout)
        widgets.jslink((self.pdb_slider, 'value'), (self.pdb_entry, 'value'))
        self.pdb_slider.observe(self.__update_pdb, 'value')
        
        self.mix_mode = widgets.Label(self.data.mix_mode, layout=widgets.Layout(flex='auto'))
        self.eff_fs = widgets.Label(("Effective Fs: " + str(self.data.effective_fs)), layout=widgets.Layout(flex='auto'))
        
        self.param_controls = widgets.Accordion([widgets.VBox([
            widgets.HBox([self.fs_label, self.fs_slider, self.fs_entry, self.fs_units]),
            widgets.HBox([self.fc_label, self.fc_slider, self.fc_entry, self.fc_units]),
            widgets.HBox([self.pll_label, self.pll_slider, self.pll_entry, self.pll_units]),
            widgets.HBox([self.nco_label, self.nco_slider, self.nco_entry, self.nco_units]),
            widgets.HBox([self.itrp_label, self.itrp_blank, self.itrp_entry, self.itrp_units]),
            widgets.HBox([self.sinc_label, self.sinc_blank, self.sinc_entry, self.sinc_units])])
        ])
        self.param_controls.set_title(0, "RF-DC Parameters")

        self.amp_controls = widgets.Accordion([widgets.VBox([
            widgets.HBox([self.hd2_label, self.hd2_slider, self.hd2_entry, self.hd2_units]),
            widgets.HBox([self.hd3_label, self.hd3_slider, self.hd3_entry, self.hd3_units]),
            widgets.HBox([self.pdb_label, self.pdb_slider, self.pdb_entry, self.pdb_units])])
        ])
        self.amp_controls.set_title(0, "Spur Amplitude")

        self.params = widgets.VBox([
            self.param_controls,
            self.amp_controls,
            widgets.HBox([self.mix_mode]),
            widgets.HBox([self.eff_fs])
        ])
        
        self.layout = widgets.HBox([self.params, self._plot])
        
    def __update_fs(self, change):
        self.data.fs_rf = change['new']
        self.__update_plot()
            
    def __update_fc(self, change):
        self.data.fc = change['new']
        self.__update_plot()
        
    def __update_pll(self, change):
        self.data.pll_ref = change['new']
        self.__update_plot()
        
    def __update_nco(self, change):
        self.data.nco = change['new']
        self.__update_plot()
        
    def __update_itrp(self, change):
        self.data.interp_rate = int(change['new'])
        self.__update_plot()
        
    def __update_sinc(self, change):
        if change['new'] == "ON":
            self.data.inv_sinc = True
        else:
            self.data.inv_sinc = False
        self.__update_plot()
        
    def __update_hd2(self, change):
        self.data.hd2_db = change['new']
        self.__update_plot()
        
    def __update_hd3(self, change):
        self.data.hd3_db = change['new']
        self.__update_plot()
        
    def __update_pdb(self, change):
        self.data.pll_db = change['new']
        self.__update_plot()
        
    def __setup_plot(self):      
        spurs_list = [self.data.nyquist_up, self.data.nyquist_down, self.data.hd2, self.data.hd2_image, 
                     self.data.hd3, self.data.hd3_image, self.data.pll_mix_up, self.data.pll_mix_up_image,
                     self.data.pll_mix_down, self.data.pll_mix_down_image, self.data.fund, self.data.fimag]

        plot_items = [go.Scatter(x=[d['x'], d['x']], y=[d['ymin'], d['ymax']], name=d['label'], hovertext=d['label'], hoverinfo='text+x') for d in spurs_list]

        plot = go.FigureWidget(plot_items)
        
        plot.update_layout(
            title={'text':"Digital Up Converter (DUC)", 'x':0.5, 'y':0.9, 'xanchor':'center', 'yanchor':'top'},
            xaxis_title={'text':"Frequency (MHz)"},
            yaxis_title={'text':"Amplitude (dB)"},
            width=900,
            height=500
        )
        
        plot.add_hline(y=0, line=dict(color='grey'))
        
        return plot
    
    def __update_plot(self):
        spurs_list = [self.data.nyquist_up, self.data.nyquist_down, self.data.hd2, self.data.hd2_image, 
                     self.data.hd3, self.data.hd3_image, self.data.pll_mix_up, self.data.pll_mix_up_image,
                     self.data.pll_mix_down, self.data.pll_mix_down_image, self.data.fund, self.data.fimag]
        
        with self._plot.batch_update():
            for i in range(len(spurs_list)):
                self._plot.data[i].x = [spurs_list[i]['x'], spurs_list[i]['x']]
                self._plot.data[i].y = [spurs_list[i]['ymin'], spurs_list[i]['ymax']]
                
        self.mix_mode.value = self.data.mix_mode
        self.eff_fs.value = ("Effective Fs: " + str(self.data.effective_fs))
