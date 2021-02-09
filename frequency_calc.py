import numpy as np

class FrequencyPlannerADC:

    def __init__(self, fs_rf=3800.0, fc=1800.0, fs_bw=20.0, pll_ref=409.2, il_factor=8):
        self.fs_rf = fs_rf
        self.fc = fc
        self.fs_bw = fs_bw
        self.pll_ref = pll_ref
        self.il_factor = il_factor
        
        self.f = np.linspace(-0.5,0.5,101)
        
    def __signal_f(self):
        fs_rf = self.fs_rf
        fs_bw = self.fs_bw
        fc = self.fc
        f = self.f
        
        ax_x = [fs_rf - ((fc+fs_bw*i) % fs_rf) if ((fc+fs_bw*i) % fs_rf) >= fs_rf/2 else ((fc+fs_bw*i) % fs_rf) for i in f]
        
        return ax_x

    def __interf_f(self):
        fc = self.fc
        fs_bw = self.fs_bw
        f = self.f
        return [fc+(fs_bw*i) for i in f]
    
    @property
    def rx_band(self):
        ax_x = self.__signal_f()
        ax_y = 6
        
        return {'label': 'RX Band', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#5a82ca'}
    
    def __hd(self, hd_num):
        fs_rf = self.fs_rf
        interf_f = self.__interf_f()
        
        ax_x = [fs_rf - (hd_num*i % fs_rf) if hd_num*i % fs_rf >= fs_rf/2 else (hd_num*i % fs_rf) for i in interf_f]
        
        return ax_x
    
    @property
    def hd2(self):
        hd_num = 2
        ax_x = self.__hd(hd_num)
        ax_y = hd_num
        
        return {'label': 'HD2', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#ed7d31'}
    
    @property
    def hd3(self):
        hd_num = 3
        ax_x = self.__hd(hd_num)
        ax_y = hd_num
        
        return {'label': 'HD3', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#a4a4a4'}
    
    @property
    def hd4(self):
        hd_num = 4
        ax_x = self.__hd(hd_num)
        ax_y = hd_num
        
        return {'label': 'HD4', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#febf00'}
    
    @property
    def hd5(self):
        hd_num = 5
        ax_x = self.__hd(hd_num)
        ax_y = hd_num
        
        return {'label': 'HD5', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#5b9ad4'}
    
    @property
    def il_rx1(self):
        fs_rf = self.fs_rf
        signal_f = self.__signal_f()
        il_factor = self.il_factor
        
        ax_y = 0.4
        
        if il_factor > 1:
            ax_x = [abs(fs_rf/2 - i) for i in signal_f]
        else:
            ax_x = [i*0 for i in signal_f]
            
        return {'label': 'IL RX1', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#70ac47'}
    
    @property
    def il_rx2(self):
        fs_rf = self.fs_rf
        signal_f = self.__signal_f()
        il_factor = self.il_factor
        
        ax_y = 0.5
        
        if il_factor > 2:
            ax_x = [abs(fs_rf/4 - i) for i in signal_f]
        else:
            ax_x = [i*0 for i in signal_f]
            
        return {'label': 'IL RX2', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#264478'}
    
    @property
    def il_rx3(self):
        fs_rf = self.fs_rf
        signal_f = self.__signal_f()
        il_factor = self.il_factor
        
        ax_y = 0.6
        
        if il_factor > 2:
            ax_x = [abs(fs_rf/4 + i) if ((fs_rf/4 + i) < fs_rf/2) else abs(fs_rf/4*3-i) for i in signal_f]
        else:
            ax_x = [i*0 for i in signal_f]
            
        return {'label': 'IL RX3', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#9d480e'}
    
    @property
    def il_rx4(self):
        fs_rf = self.fs_rf
        signal_f = self.__signal_f()
        il_factor = self.il_factor
        
        ax_y = 0.7
        
        if il_factor > 4:
            ax_x = [abs(fs_rf/8 - i) for i in signal_f]
        else:
            ax_x = [i*0 for i in signal_f]
            
        return {'label': 'IL RX4', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#636363'}
    
    @property
    def il_rx5(self):
        fs_rf = self.fs_rf
        signal_f = self.__signal_f()
        il_factor = self.il_factor
        
        ax_y = 0.8
        
        if il_factor > 2:
            ax_x = [abs(fs_rf/8 + i) if ((fs_rf/8 + i) < fs_rf/2) else abs(fs_rf/8*7-i) for i in signal_f]
        else:
            ax_x = [i*0 for i in signal_f]
            
        return {'label': 'IL RX5', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#987300'}
    
    @property
    def fs8_p_hd3(self):
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        hd3 = self.__hd(3)
        
        ax_y = 3.5
        
        if il_factor > 4:
            ax_x = [abs(fs_rf/8+i) if (fs_rf/8+i < fs_rf/2) else abs(fs_rf/8*7-i) for i in hd3]
        else:
            ax_x = [i*0 for i in hd3]
            
        return {'label': 'FS/8+HD3', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#d16012'}
    
    @property
    def fs8_m_hd3(self):
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        hd3 = self.__hd(3)
        
        ax_y = 3.5
        
        if il_factor > 4:
            ax_x = [abs(fs_rf/8-i) for i in hd3]
        else:
            ax_x = [i*0 for i in hd3]
            
        return {'label': 'FS/8-HD3', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#335aa0'}
    
    @property
    def fs8_p_hd2(self):
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        hd2 = self.__hd(2)
        
        ax_y = 2.5
        
        if il_factor > 4:
            ax_x = [abs(fs_rf/8+i) if (fs_rf/8+i < fs_rf/2) else abs(fs_rf/8*7-i) for i in hd2]
        else:
            ax_x = [i*0 for i in hd2]
            
        return {'label': 'FS/8+HD2', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#8bc068'}
    
    @property
    def fs8_m_hd2(self):
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        hd2 = self.__hd(2)
        
        ax_y = 2.5
        
        if il_factor > 4:
            ax_x = [abs(fs_rf/8-i) for i in hd2]
        else:
            ax_x = [i*0 for i in hd2]
            
        return {'label': 'FS/8-HD2', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#7caedc'}
    
    @property
    def fs4_p_hd3(self):
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        hd3 = self.__hd(3)
        
        ax_y = 3.5
        
        if il_factor > 2:
            ax_x = [abs(fs_rf/4+i) if (fs_rf/4+i < fs_rf/2) else abs(fs_rf/4*3-i) for i in hd3]
        else:
            ax_x = [i*0 for i in hd3]
            
        return {'label': 'FS/4+HD3', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#fecc33'}
    
    @property
    def fs4_m_hd3(self):
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        hd3 = self.__hd(3)
        
        ax_y = 3.5
        
        if il_factor > 2:
            ax_x = [abs(fs_rf/4-i) for i in hd3]
        else:
            ax_x = [i*0 for i in hd3]
            
        return {'label': 'FS/4-HD3', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#b6b6b6'}
    
    @property
    def fs4_p_hd2(self):
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        hd2 = self.__hd(2)
        
        ax_y = 2.5
        
        if il_factor > 2:
            ax_x = [abs(fs_rf/4+i) if (fs_rf/4+i < fs_rf/2) else abs(fs_rf/4*3-i) for i in hd2]
        else:
            ax_x = [i*0 for i in hd2]
            
        return {'label': 'FS/4+HD2', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#698dcf'}
    
    @property
    def fs4_m_hd2(self):
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        hd2 = self.__hd(2)
        
        ax_y = 2.5
        
        if il_factor > 2:
            ax_x = [abs(fs_rf/4-i) for i in hd2]
        else:
            ax_x = [i*0 for i in hd2]
            
        return {'label': 'FS/4-HD2', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#00fe35'}
    
    @property
    def fs2_m_hd3(self):
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        hd3 = self.__hd(3)
        
        ax_y = 3.5
        
        if il_factor > 1:
            ax_x = [fs_rf/2-i for i in hd3]
        else:
            ax_x = fs2_m_hd3 = [i*0 for i in hd3]
            
        return {'label': 'FS/2-HD3', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#f0965a'}
    
    @property
    def fs2_m_hd2(self):
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        hd2 = self.__hd(2)
        
        ax_y = 2.5
        
        if il_factor > 1:
            ax_x = [abs(fs_rf/2-i) for i in hd2]
        else:
            ax_x = fs2_m_hd3 = [i*0 for i in hd2]
            
        return {'label': 'FS/2-HD2', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#255e90'}


    @property
    def pll_mix_up(self):
        fs_rf = self.fs_rf
        fc = self.fc
        fs_bw = self.fs_bw
        pll_ref = self.pll_ref
        f = self.f
        
        ax_y = 4.5
        ax_x = [fs_rf - ((fc+fs_bw*i+pll_ref) % fs_rf) if ((fc+fs_bw*i+pll_ref) % fs_rf) >= fs_rf/2 else ((fc+fs_bw*i+pll_ref) % fs_rf) for i in f]
        
        return {'label': 'PLL Mix Up', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#CB9900'}
    
    @property
    def pll_mix_down(self):
        fs_rf = self.fs_rf
        fc = self.fc
        fs_bw = self.fs_bw
        pll_ref = self.pll_ref
        f = self.f
        
        ax_y = 4.5
        ax_x = [fs_rf - ((fc+fs_bw*i-pll_ref) % fs_rf) if ((fc+fs_bw*i-pll_ref) % fs_rf) >= fs_rf/2 else ((fc+fs_bw*i-pll_ref) % fs_rf) for i in f]
        
        return {'label': 'PLL Mix Down', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin': 0, 'ymax':ax_y, 'color':'#327dc1'}
    
    @property
    def nyquist(self):
        ax_x = self.fs_rf/2
        ax_y = 6
        
        return {'label': 'Nyquist', 'xmin':ax_x, 'xmax':ax_x, 'ymin': 0, 'ymax':ax_y, 'color':'#838383'}
    
    @property
    def calibration_mode(self):
        fs_rf = self.fs_rf
        fc = self.fc
        
        if ((fs_rf/2*0.7 < fc) and (fc < fs_rf/2*1.3)) or ((fs_rf/2*3-0.3*fs_rf/2 < fc) and (fc < fs_rf/2*3+0.3*fs_rf/2)) or ((fs_rf/2*5-0.3*fs_rf/2 < fc) and (fc < fs_rf/2*5+0.3*fs_rf/2)) or ((fs_rf/2*7-0.3*fs_rf/2 < fc) and (fc < fs_rf/2*7+0.3*fs_rf/2)) or ((fs_rf/2*9+0.3*fs_rf/2 < fc) and (fc < fs_rf/2*9+0.3*fs_rf/2)):
            return "Calibration Mode: Mode 1"
        else:
            return "Calibration Mode: Mode 2"

class FrequencyPlannerDAC:
    
    def __init__(self, fs_rf=3800, fc=1800, fs_bw=20.0, pll_ref=409.2):
        self.fs_rf = fs_rf
        self.fc = fc
        self.fs_bw = fs_bw
        self.pll_ref = pll_ref

        self.f = np.linspace(-0.5,0.5,101)

    def __signal_f(self):
        fs_rf = self.fs_rf
        fs_bw = self.fs_bw
        fc = self.fc
        f = self.f

        return [fc + (fs_bw*i) for i in f]
    
    @property
    def tx_band(self):
        ax_x = self.__signal_f()
        ax_y = 8
        
        return {'label':'TX Band', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#5a82ca', 'linestyle':'solid'}
    
    @property
    def nyquist(self):
        ax_x = self.fs_rf/2
        ax_y = 8
        
        return {'label':'Nyquist 1', 'xmin':ax_x, 'xmax':ax_x, 'ymin':0, 'ymax':ax_y, 'color':'#838383', 'linestyle':'solid'}
    
    @property
    def nyquist_image(self):
        ax_x = self.fs_rf
        ax_y = 8
        
        return {'label':'Nyquist 2', 'xmin':ax_x, 'xmax':ax_x, 'ymin':0, 'ymax':ax_y, 'color':'#494949', 'linestyle':'solid'}
    
    def __hd_nyq1(self, hd_num):
        nyq_rf = self.fs_rf/2
        signal_f = self.__signal_f()
        
        ax_x = [(i*hd_num % nyq_rf) if ((np.floor((i*hd_num)/nyq_rf) % 2)  == 0) else (nyq_rf - (i*hd_num % nyq_rf)) for i in signal_f]
#         print([(int((i*hd_num)/nyq_rf) % 2) for i in signal_f])
        
        return ax_x
    
    def __hd_nyq2(self, hd_num):
        hd = self.__hd_nyq1(hd_num)
        
        ax_x = [self.fs_rf - i for i in hd]
        
        return ax_x
    
    @property
    def hd2_nyq1(self):
        hd_num = 2
        ax_x = self.__hd_nyq1(hd_num)
        ax_y = hd_num
        
        return {'label':'HD2', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#ed7d31', 'linestyle':'solid'}
    
    @property
    def hd3_nyq1(self):
        hd_num = 3
        ax_x = self.__hd_nyq1(hd_num)
        ax_y = hd_num
        
        return {'label':'HD3', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#a4a4a4', 'linestyle':'solid'}
    
    @property
    def hd4_nyq1(self):
        hd_num = 4
        ax_x = self.__hd_nyq1(hd_num)
        ax_y = hd_num
        
        return {'label':'HD4', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#febf00', 'linestyle':'solid'}
    
    @property
    def hd5_nyq1(self):
        hd_num = 5
        ax_x = self.__hd_nyq1(hd_num)
        ax_y = hd_num
        
        return {'label':'HD5', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#5b9ad4', 'linestyle':'solid'}
    
    @property
    def hd2_nyq2(self):
        hd_num = 2
        ax_x = self.__hd_nyq2(hd_num)
        ax_y = hd_num
        
        return {'label':'HD2 Image', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#70ad47', 'linestyle':'solid'}
    
    @property
    def hd3_nyq2(self):
        hd_num = 3
        ax_x = self.__hd_nyq2(hd_num)
        ax_y = hd_num
        
        return {'label':'HD3 Image', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#264478', 'linestyle':'solid'}
    
    @property
    def hd4_nyq2(self):
        hd_num = 4
        ax_x = self.__hd_nyq2(hd_num)
        ax_y = hd_num
        
        return {'label':'HD4 Image', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#9e480e', 'linestyle':'solid'}
    
    @property
    def hd5_nyq2(self):
        hd_num = 5
        ax_x = self.__hd_nyq2(hd_num)
        ax_y = hd_num
        
        return {'label':'HD5 Image', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#636363', 'linestyle':'solid'}
    
    def __fimg(self):
        signal_f = self.__signal_f()
        nyq_rf = self.fs_rf/2
        
        ax_x = [(2*nyq_rf - i) if (int(i/nyq_rf) % 2 == 0) else (nyq_rf - (i % nyq_rf)) for i in signal_f]
        
        return ax_x
    
    @property
    def fimg(self):        
        ax_x = self.__fimg()
        ax_y = 8
        
        return {'label':'Tx Band Image', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#c46728', 'linestyle':'solid'}
    
    @property
    def pll_mix_up(self):
        signal_f = self.__signal_f()
        
        ax_x = [(i + self.pll_ref) for i in signal_f]
        ax_y = 6.5
        
        return {'label':'PLL Mix Up', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#CB9900', 'linestyle':'solid'}
    
    @property
    def pll_mix_up_image(self):
        fimag = self.__fimg()
        
        ax_x = [(i + self.pll_ref) for i in fimag]
        ax_y = 6.5
        
        return {'label':'PLL Mix Up Image', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#b1bcdf', 'linestyle':'solid'}
    
    @property
    def pll_mix_down(self):
        signal_f = self.__signal_f()
        
        ax_x = [abs(i - self.pll_ref) for i in signal_f]
        ax_y = 6.5
        
        return {'label':'PLL Mix Down', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#327dc1', 'linestyle':'solid'}
    
    @property
    def pll_mix_down_image(self):
        fimg = self.__fimg()
        
        ax_x = [abs(i - self.pll_ref) for i in fimg]
        ax_y = 6.5
        
        return {'label':'PLL Mix Down Image', 'xmin':min(ax_x), 'xmax':max(ax_x), 'ymin':0, 'ymax':ax_y, 'color':'#f2b7a3', 'linestyle':'solid'}
    
    @property
    def mix_mode(self):
        if self.fc > (self.fs_rf/2):
            return "Mix Mode: ON"
        else:
            return "Mix Mode: OFF"
    
    @property
    def get_dicts(self):
        
        dict_list = [self.tx_signal, 
                     self.hd2_nyq1, self.hd3_nyq1, self.hd4_nyq1, self.hd5_nyq1, 
                     self.hd2_nyq2, self.hd3_nyq2, self.hd4_nyq2, self.hd5_nyq2, 
                     self.pll_mix_up, self.pll_mix_up_image, 
                     self.pll_mix_down, self.pll_mix_down_image, 
                     self.nyquist, self.nyquist_image]
        
        x_max = max([i['xmax'] for i in dict_list])
        x_max = x_max + x_max*0.2
        x_min = min([i['xmin'] for i in dict_list])
        x_min = x_min + x_min*0.2
        
        y_max = 9
        y_min = 0
        
        init_dict = {'label':'init', 'xmin':x_min, 'xmax':x_max, 'ymin':y_min, 'ymax':y_max}
        
        return [init_dict] + dict_list

class FrequencyPlannerDDC:
    def __init__(self, fs_rf=3800, il_factor=8, fc=1800, dec=1, nco=1800, hd2_db=70, hd3_db=70, tis_spur_db=85, off_spur_db=82, pll_mix_db=70, pll_ref=409.2, nsd_db=-154):
        self.fs_rf = fs_rf
        self.il_factor = il_factor
        self.fc = fc
        self.dec = dec
        self.nco = nco
        self.hd2_db = hd2_db
        self.hd3_db = hd3_db
        self.tis_spur_db = tis_spur_db
        self.off_spur_db = off_spur_db
        self.pll_mix_db = pll_mix_db
        self.pll_ref = pll_ref
        self.nsd_db = nsd_db
    
    @property
    def noisefloor(self):
        return (self.nsd_db + 10*np.log10(self.fs_rf * 10**6 / 2) - 10*np.log10(16384/2))
        
    @property
    def rx_alias(self):
        fs_rf = self.fs_rf
        fc = self.fc
        dec = self.dec
        nco = self.nco
        
        alias_fs = (fs_rf - (fc % fs_rf)) if ((fc % fs_rf) >= fs_rf/2) else (fc % fs_rf) #BE16
        nco_shift = alias_fs + nco #BH16
        
        ax_x = (nco_shift - int((nco_shift - fs_rf/dec/2)/(fs_rf/dec)) * (fs_rf/dec)) if nco_shift < 0 else (nco_shift - int((nco_shift + fs_rf/dec/2)/(fs_rf/dec))*(fs_rf/dec)) #BK16
        ax_y = 0
        
        return {'label':'Fc', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#5a82ca', 'linestyle':'solid'}
    
    @property
    def rx_image(self):
        fs_rf = self.fs_rf
        fc = self.fc
        nco = self.nco
        dec = self.dec
        
        alias_fs = (fs_rf - (fc % fs_rf)) if ((fc % fs_rf) >= fs_rf/2) else (fc % fs_rf) #BE16
        image_fs = fs_rf - alias_fs #BF16
        nco_shift = image_fs + nco #BI16
        
        ax_x = (nco_shift - int((nco_shift - fs_rf/dec/2)/(fs_rf/dec)) * (fs_rf/dec)) if nco_shift < 0 else (nco_shift - int((nco_shift + fs_rf/dec/2)/(fs_rf/dec))*(fs_rf/dec)) #BL16
        ax_y = 0
        
        return {'label':'Fc Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#c46728', 'linestyle':'solid'}
    
    def __hd(self, hd_num):
        fs_rf = self.fs_rf
        fc = self.fc
        nco = self.nco
        dec = self.dec
        
        alias_fs = (fs_rf - (hd_num*fc % fs_rf)) if (hd_num*fc % fs_rf >= fs_rf/2) else (hd_num*fc % fs_rf) #BE21
        nco_shift = alias_fs + nco #BH21
        
        ax_x = (nco_shift - int((nco_shift - fs_rf/dec/2)/(fs_rf/dec)) * (fs_rf/dec)) if nco_shift < 0 else (nco_shift - int((nco_shift + fs_rf/dec/2)/(fs_rf/dec))*(fs_rf/dec)) 
        
        return ax_x
    
    def __hd_image(self, hd_num):
        fs_rf = self.fs_rf
        fc = self.fc
        nco = self.nco
        dec = self.dec
        
        alias_fs = (fs_rf - (hd_num*fc % fs_rf)) if (hd_num*fc % fs_rf >= fs_rf/2) else (hd_num*fc % fs_rf) #BE21
        image_fs = fs_rf - alias_fs
        nco_shift = image_fs + nco
        
        ax_x = (nco_shift - int((nco_shift - fs_rf/dec/2)/(fs_rf/dec)) * (fs_rf/dec)) if nco_shift < 0 else (nco_shift - int((nco_shift + fs_rf/dec/2)/(fs_rf/dec))*(fs_rf/dec)) 
        
        return ax_x
    
    @property
    def hd2(self):
        ax_x = self.__hd(2)
        ax_y = -self.hd2_db
        return {'label':'HD2', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#ed7d31', 'linestyle':'solid'}
    
    @property
    def hd2_image(self):
        ax_x = self.__hd_image(2)
        ax_y = -self.hd2_db
        return {'label':'HD2 Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#70ad47', 'linestyle':'solid'}
    
    @property
    def hd3(self):
        ax_x = self.__hd(3)
        ax_y = -self.hd3_db
        
        return {'label':'HD3', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#a4a4a4', 'linestyle':'solid'}
    
    @property
    def hd3_image(self):
        ax_x = self.__hd_image(3)
        ax_y = -self.hd3_db
        
        return {'label':'HD3 Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#264478', 'linestyle':'solid'}
    
    @property
    def offset_spur(self):
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        dec = self.dec
        nco = self.nco
        
        alias_fs = (fs_rf/il_factor) if (il_factor==4 or il_factor==8) else (0) #BE26
        nco_shift = alias_fs + nco #BH26
        
        ax_x = 0
        ax_y = -self.off_spur_db
        
        if il_factor==4 or il_factor==8:
            if nco_shift<0:
                ax_x = nco_shift-(int((nco_shift-fs_rf/dec/2)/(fs_rf/dec))*(fs_rf/dec))
            else:
                ax_x = nco_shift-(int((nco_shift+fs_rf/dec/2)/(fs_rf/dec))*fs_rf/dec)
        else: 
            ax_x = -fs_rf/dec/2
            
        return {'label':'Offset Spur', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#669645', 'linestyle':'solid'}
    
    @property
    def offset_spur_image(self):
        
        fs_rf = self.fs_rf
        il_factor = self.il_factor
        dec = self.dec
        nco = self.nco
        
        alias_fs = (fs_rf/il_factor) if (il_factor==4 or il_factor==8) else (0) #BE26
        image_fs =  (fs_rf - alias_fs) if (il_factor==4 or il_factor==8) else (0) #BF26
        nco_shift = image_fs + nco
        
        ax_x = 0
        ax_y = -self.off_spur_db
        
        if il_factor==4 or il_factor==8:
            if nco_shift<0:
                ax_x = nco_shift-(int((nco_shift-fs_rf/dec/2)/(fs_rf/dec))*(fs_rf/dec))
            else:
                ax_x = nco_shift-(int((nco_shift+fs_rf/dec/2)/(fs_rf/dec))*fs_rf/dec)
        else: 
            ax_x = -fs_rf/dec/2
            
        return {'label':'Offset Spur Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#ed7d31', 'linestyle':'solid'}
    
    @property
    def tis_spur(self):
        fs_rf = self.fs_rf
        fc = self.fc
        nco = self.nco
        il_factor = self.il_factor
        dec = self.dec
        
        alias_fs = (fs_rf - (fc % fs_rf)) if ((fc % fs_rf) >= fs_rf/2) else (fc % fs_rf) #BE16
        
        alias_fs_spur = 0
        
        if il_factor > 1: #BE18
            if (fs_rf/2 - alias_fs) % fs_rf >= fs_rf/2:
                alias_fs_spur = fs_rf - ((fs_rf/2-alias_fs) % fs_rf)
            else:
                alias_fs_spur = (fs_rf/2-alias_fs) % fs_rf
        else:
            alias_fs_spur = 0
            
        nco_shift = alias_fs_spur + nco #BH18
        
        ax_x = 0 #BK18
        ax_y = -self.tis_spur_db
        
        if il_factor>1:
            if nco_shift<0:
                ax_x = nco_shift-(int((nco_shift-fs_rf/dec/2)/(fs_rf/dec))*(fs_rf/dec))
            else:
                ax_x = nco_shift-(int((nco_shift+fs_rf/dec/2)/(fs_rf/dec))*fs_rf/dec)
        else:
            ax_x = -fs_rf/dec/2
            
        return {'label':'TI Spur', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#a5a5a5', 'linestyle':'solid'}
    
    @property
    def tis_spur_image(self):
        fs_rf = self.fs_rf
        fc = self.fc
        nco = self.nco
        il_factor = self.il_factor
        dec = self.dec
        
        alias_fs = (fs_rf - (fc % fs_rf)) if ((fc % fs_rf) >= fs_rf/2) else (fc % fs_rf) #BE16
        
        alias_fs_spur = 0 #BE18
        
        if il_factor > 1:
            if (fs_rf/2 - alias_fs) % fs_rf >= fs_rf/2:
                alias_fs_spur = fs_rf - ((fs_rf/2-alias_fs) % fs_rf)
            else:
                alias_fs_spur = (fs_rf/2-alias_fs) % fs_rf
        else:
            alias_fs_spur = 0
        
        image_fs_spur = (fs_rf - alias_fs_spur) if (il_factor > 1) else (0) #BF18
        
        nco_shift = image_fs_spur + nco #BI18
        
        ax_x = 0 #BL18
        ax_y = -self.tis_spur_db
        
        if il_factor>1:
            if nco_shift<0:
                ax_x = nco_shift-(int((nco_shift-fs_rf/dec/2)/(fs_rf/dec))*(fs_rf/dec))
            else:
                ax_x = nco_shift-(int((nco_shift+fs_rf/dec/2)/(fs_rf/dec))*fs_rf/dec)
        else:
            ax_x = -fs_rf/dec/2
            
        return {'label':'TI Spur Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#ffc000', 'linestyle':'solid'}
    
    @property
    def pll_mix_up(self):
        fc = self.fc
        fs_rf = self.fs_rf
        dec = self.dec
        nco = self.nco
        pll_ref = self.pll_ref
        
        fs_alias = (fs_rf - (fc+pll_ref)%(fs_rf)) if ((fc+pll_ref)%(fs_rf) >= (fs_rf/2)) else ((fc+pll_ref) % (fs_rf)) #BE35
        nco_shift = fs_alias + nco #BH35
        
        ax_x = (nco_shift - int((nco_shift-(fs_rf/dec/2))/(fs_rf/dec)) * (fs_rf/dec)) if (nco_shift<0) else (nco_shift - int((nco_shift+(fs_rf/dec/2))/(fs_rf/dec)) * (fs_rf/dec)) #BK35
        ax_y = -self.pll_mix_db
        
        return {'label':'PLL Mix Up', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#CB9900', 'linestyle':'solid'}
    
    @property
    def pll_mix_up_image(self):
        fc = self.fc
        fs_rf = self.fs_rf
        dec = self.dec
        nco = self.nco
        pll_ref = self.pll_ref
        
        fs_alias = (fs_rf - (fc+pll_ref)%(fs_rf)) if ((fc+pll_ref)%(fs_rf) >= (fs_rf/2)) else ((fc+pll_ref) % (fs_rf)) #BE35
        fs_image = fs_rf - fs_alias #BF35
        nco_shift = fs_image + nco #BI35
        
        ax_x = (nco_shift - int((nco_shift-(fs_rf/dec/2))/(fs_rf/dec)) * (fs_rf/dec)) if (nco_shift<0) else (nco_shift - int((nco_shift+(fs_rf/dec/2))/(fs_rf/dec)) * (fs_rf/dec)) #BK35
        ax_y = -self.pll_mix_db
        
        return {'label':'PLL Mix Up Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#b1bcdf', 'linestyle':'#0906D9'}
    
    @property
    def pll_mix_down(self):
        fc = self.fc
        fs_rf = self.fs_rf
        dec = self.dec
        nco = self.nco
        pll_ref = self.pll_ref
        
        fs_alias = (fs_rf - (fc-pll_ref)%(fs_rf)) if ((fc-pll_ref)%(fs_rf) >= (fs_rf/2)) else ((fc-pll_ref) % (fs_rf)) #BE36
        nco_shift = fs_alias + nco #BH36
        
        ax_x = (nco_shift - int((nco_shift-(fs_rf/dec/2))/(fs_rf/dec)) * (fs_rf/dec)) if (nco_shift<0) else (nco_shift - int((nco_shift+(fs_rf/dec/2))/(fs_rf/dec)) * (fs_rf/dec)) #BK35
        ax_y = -self.pll_mix_db
        
        return {'label':'PLL Mix Down', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#327dc1', 'linestyle':'solid'}
    
    @property
    def pll_mix_down_image(self):
        fc = self.fc
        fs_rf = self.fs_rf
        dec = self.dec
        nco = self.nco
        pll_ref = self.pll_ref
        
        fs_alias = (fs_rf - (fc-pll_ref)%(fs_rf)) if ((fc-pll_ref)%(fs_rf) >= (fs_rf/2)) else ((fc-pll_ref) % (fs_rf)) #BE36
        fs_image = fs_rf - fs_alias #BF35
        nco_shift = fs_image + nco #BH36
        
        ax_x = (nco_shift - int((nco_shift-(fs_rf/dec/2))/(fs_rf/dec)) * (fs_rf/dec)) if (nco_shift<0) else (nco_shift - int((nco_shift+(fs_rf/dec/2))/(fs_rf/dec)) * (fs_rf/dec)) #BK35
        ax_y = -self.pll_mix_db
        
        return {'label':'PLL Mix Down Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#f2b7a3', 'linestyle':'solid'}
    
    @property
    def nyquist_up(self):
        ax_x = self.fs_rf/self.dec/2
        ax_y = 0
        
        return {'label':'Nyquist 1', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#838383', 'linestyle':'solid'}
    
    @property
    def nyquist_down(self):
        ax_x = -self.fs_rf/self.dec/2
        ax_y = 0
        
        return {'label':'Nyquist 2', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#494949', 'linestyle':'dashed'}

class FrequencyPlannerDUC:
    def __init__(self, fs_rf=3800, fc=1800, nco=1800, interp_rate=1, inv_sinc=True, hd2_db=65, hd3_db=75, pll_db=72, pll_ref=409.2):
        self.fs_rf = fs_rf
        self.fc = fc
        self.nco = nco
        self.interp_rate = interp_rate
        self.inv_sinc = inv_sinc
        self.hd2_db = hd2_db
        self.hd3_db = hd3_db
        self.pll_db = pll_db
        self.pll_ref = pll_ref
    
    @property
    def noisefloor(self):
        return -155 + 10*np.log10(self.fs_rf*10**6 /2) - 10*np.log10(16384/2)
        
    def __get_freq_resp(self):
        
        ideal_sinc = [-0.000357195832004,-0.001428818584301,-0.003214974042325,-0.005715838570397,-0.008931659194662,-0.012862753719357,-0.017509510876466,-0.022872390508981,-0.028951923787906,-0.035748713463276,-0.043263434149413,-0.05149683264475,-0.060449728286532,-0.070123013340798,-0.080517653428007,-0.091634687984817,-0.10347523076246,-0.116040470362259,-0.129331670808878,-0.143350172161876,-0.158097391166273,-0.173574821942797,-0.18978403671858,-0.20672668659909,-0.224404502382154,-0.242819295414975,-0.261972958495077,-0.281867466816209,-0.30250487896024,-0.323887337936199,-0.346017072267623,-0.36889639712946,-0.392527715535842,-0.416913519580108,-0.442056391728534,-0.467959006169282,-0.494624130218195,-0.522054625783085,-0.550253450888335,-0.579223661261618,-0.608968411984735,-0.639490959210573,-0.670794661948375,-0.702882983919528,-0.735759495486291,-0.769427875655899,-0.803891914162667,-0.839155513630834,-0.875222691821013,-0.912097583963241,-0.949784445179813,-0.988287653001208,-1.02761170997859,-1.06776124639652,-1.10874102308979,-1.1505559343683,-1.19321101105433,-1.23671142363656,-1.28106248554561,-1.32626965655597,-1.37233854631945,-1.41927491803567,-1.4670846922653,-1.51577395089203,-1.5653489412396,-1.61581608035067,-1.6671819594344,-1.71945334849035,-1.7726372011162,-1.82674065950797,-1.88177105966088,-1.93773593678051,-1.99464303091361,-2.05250029280881,-2.11131589001814,-2.17109821325062,-2.23185588299001,-2.29359775638939,-2.35633293445618,-2.42007076954167,-2.48482087315026,-2.55059312408441,-2.61739767694218,-2.68524497098533,-2.7541457393971,-2.82411101894982,-2.89515216010387,-2.96728083756077,-3.04050906129469,-3.11484918808815,-3.19031393359928,-3.26691638498999,-3.34467001414609,-3.42358869152242,-3.50368670064862,-3.584978753333,-3.66748000560498,-3.75120607443905,-3.83617305530635,-3.92239754060305]
        corrected_resp = [0.00002768,0.00010804,0.00023316,0.00039020,0.00056195,0.00072760,0.00086360,0.00094473,0.00094522,0.00083995,0.00060567,0.00022214,-0.00032673,-0.00105189,-0.00195832,-0.00304439,-0.00430138,-0.00571331,-0.00725698,-0.00890227,-0.01061270,-0.01234628,-0.01405649,-0.01569363,-0.01720617,-0.01854235,-0.01965184,-0.02048742,-0.02100668,-0.02117362,-0.02096014,-0.02034736,-0.01932670,-0.01790068,-0.01608346,-0.01390100,-0.01139087,-0.00860174,-0.00559246,-0.00243086,0.00080784,0.00404280,0.00718968,0.01016285,0.01287777,0.01525343,0.01721479,0.01869509,0.01963815,0.02000031,0.01975225,0.01888040,0.01738800,0.01529573,0.01264195,0.00948235,0.00588916,0.00194990,-0.00223450,-0.00655196,-0.01088201,-0.01509897,-0.01907546,-0.02268623,-0.02581220,-0.02834454,-0.03018890,-0.03126940,-0.03153252,-0.03095067,-0.02952530,-0.02728955,-0.02431033,-0.02068970,-0.01656560,-0.01211186,-0.00753746,-0.00308512,0.00097080,0.00432698,0.00665442,0.00760212,0.00680116,0.00386900,-0.00158593,-0.00995968,-0.02164813,-0.03704249,-0.05652491,-0.08046427,-0.10921231,-0.14309994,-0.18243396,-0.22749408,-0.27853027,-0.33576051,-0.39936888,-0.46950400,-0.54627782,-0.62976486]
        mixed_mode = [-3.92239754060305,-3.87345339250503,-3.82576782779785,-3.77932533320697,-3.73411089270338,-3.69010996923552,-3.64730848733834,-3.60569281657001,-3.56524975573061,-3.52596651781955,-3.48783071569165,-3.45083034837419,-3.41495378800954,-3.38018976739026,-3.34652736805577,-3.31395600892122,-3.28246543541131,-3.25204570907336,-3.22268719764529,-3.1943805655559,-3.16711676483602,-3.14088702642027,-3.11568285182051,-3.09149600515314,-3.06831850550321,-3.04614261960956,-3.02496085485592,-3.00476595255369,-2.98555088150326,-2.96730883182081,-2.95003320901903,-2.9337176283302,-2.91835590926091,-2.90394207036846,-2.89047032424923,-2.87793507272987,-2.86633090225291,-2.85565257944845,-2.84589504688425,-2.83705341898702,-2.82912297812774,-2.82209917086459,-2.81597760433719,-2.8107540428062,-2.8064244043326,-2.8029847575915,-2.80043131881505,-2.79876044885999,-2.79796865039504,-2.79805256520383,-2.79900897159923,-2.80083478194521,-2.80352704028237,-2.80708292005374,-2.81149972192733,-2.81677487171238,-2.82290591836612,-2.82989053208828,-2.83772650250048,-2.84641173690801,-2.85594425864141,-2.86632220547565,-2.87754382812447,-2.88960748880799,-2.90251165989143,-2.9162549225931,-2.93083596575983,-2.94625358470821,-2.96250668012997,-2.97959425705995,-2.99751542390529,-3.01626939153454,-3.03585547242523,-3.05627307986889,-3.07752172723231,-3.09960102727405,-3.12251069151511,-3.14625052966297,-3.17082044908808,-3.19622045435205,-3.22245064678675,-3.2495112241238,-3.27740248017363,-3.30612480455379,-3.33567868246583,-3.36606469452045,-3.39728351661042,-3.42933591983104,-3.46222277044781,-3.49594502991102,-3.53050375491724,-3.56590009751741,-3.60213530527159,-3.63921072145022,-3.67712778528201,-3.71588803224846,-3.75549309442514,-3.79594470086999,-3.83724467805865,-3.92239754060305]
        
        f_nyq1 = (np.arange(0.01,1.01,1/100)*self.fs_rf/2).tolist()
        f_nyq2 = (np.arange(0.5,1,1/100) * self.fs_rf).tolist()
        
        ax_y = 0
        
        if (self.fc+self.nco)%self.fs_rf >= self.fs_rf/2:
            ax_y = mixed_mode[f_nyq2.index(min(f_nyq2, key=lambda x:abs(x-(self.fc+self.nco))))] #analogous to Excel's LOOKUP function
        else:
            if self.inv_sinc:
                ax_y = corrected_resp[f_nyq1.index(min(f_nyq1, key=lambda x:abs(x-(self.fc+self.nco))))]
            else:
                ax_y = ideal_sinc[f_nyq1.index(min(f_nyq1, key=lambda x:abs(x-(self.fc+self.nco))))]
                
        return ax_y
        
    
    @property
    def nyquist_up(self):
        ax_x = self.fs_rf/2
        ax_y = 0
        return {'label':'Nyquist 1', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#838383', 'linestyle':'dashdot'}
    
    @property
    def nyquist_down(self):
        ax_x = self.fs_rf
        ax_y = 0
        
        return {'label':'Nyquist 2', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#494949', 'linestyle':'dashed'}
    
    def __hd(self, hd_num):
        nyq_rf = self.fs_rf/2
        fc = self.fc
        nco = self.nco
        
        signal_f = (fc + nco)*hd_num #CB21
        ax_x = (signal_f%nyq_rf) if ((np.floor(signal_f/nyq_rf))%(2) == 0) else (nyq_rf-(signal_f%nyq_rf)) #CE21
        
        return ax_x
    
    @property
    def hd2(self):
        freq_resp = self.__get_freq_resp()
        hd2_db = self.hd2_db
        
        ax_x = self.__hd(2)
        ax_y = freq_resp - hd2_db
        
        return {'label':'HD2', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#ed7d31', 'linestyle':'solid'}
    
    @property
    def hd3(self):
        freq_resp = self.__get_freq_resp()
        hd3_db = self.hd3_db
        
        ax_x = self.__hd(3)
        ax_y = freq_resp - hd3_db
        
        return {'label':'HD3', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#a4a4a4', 'linestyle':'solid'}
    
    @property
    def hd2_image(self):
        freq_resp = self.__get_freq_resp()
        hd2_db = self.hd2_db
        nyq_rf = self.fs_rf/2
        
        ax_x = 2*nyq_rf - self.__hd(2)
        ax_y = freq_resp - hd2_db
        
        return {'label':'HD2 Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#70ad47', 'linestyle':'solid'}
    
    @property
    def hd3_image(self): # this is different than Xilinx (CN51)
        freq_resp = self.__get_freq_resp()
        hd3_db = self.hd3_db
        nyq_rf = self.fs_rf/2
        
        ax_x = 2*nyq_rf - self.__hd(3)
        ax_y = freq_resp - hd3_db
        
        return {'label':'HD3 Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#264478', 'linestyle':'solid'}
    
    @property
    def pll_mix_up(self):
        fc = self.fc
        nco = self.nco
        pll_ref = self.pll_ref
        pll_db = self.pll_db
        freq_resp = self.__get_freq_resp()
        
        ax_x = (fc+nco) - pll_ref
        ax_y = freq_resp - pll_db
        
        return {'label':'PLL Mix Up', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#CB9900', 'linestyle':'solid'}
    
    @property
    def pll_mix_down(self):
        fc = self.fc
        nco = self.nco
        pll_ref = self.pll_ref
        pll_db = self.pll_db
        freq_resp = self.__get_freq_resp()
        
        ax_x = (fc+nco) + pll_ref
        ax_y = freq_resp - pll_db
        
        return {'label':'PLL Mix Down', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#327dc1', 'linestyle':'solid'}
    
    @property
    def pll_mix_up_image(self):
        nyq_rf = self.fs_rf/2
        fc = self.fc
        nco = self.nco
        pll_ref = self.pll_ref
        pll_db = self.pll_db
        freq_resp = self.__get_freq_resp()
        
        fimg = (2*nyq_rf - (fc+nco)) if (np.floor((fc+nco)/nyq_rf)%2 == 0) else (nyq_rf - ((fc+nco)%nyq_rf))
        ax_x = fimg - pll_ref
        ax_y = freq_resp - pll_db
        
        return {'label':'PLL Mix Up Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#b1bcdf', 'linestyle':'solid'}
    
    @property
    def pll_mix_down_image(self):
        nyq_rf = self.fs_rf/2
        fc = self.fc
        nco = self.nco
        pll_ref = self.pll_ref
        pll_db = self.pll_db
        freq_resp = self.__get_freq_resp()
        
        fimg = (2*nyq_rf - (fc+nco)) if (np.floor((fc+nco)/nyq_rf)%2 == 0) else (nyq_rf - ((fc+nco)%nyq_rf))
        
        ax_x = fimg + pll_ref
        ax_y = freq_resp - pll_db
        
        return {'label':'PLL Mix Down Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#f2b7a3', 'linestyle':'solid'}
    
    @property
    def fund(self):
        ax_x = self.fc + self.nco
        ax_y = self.__get_freq_resp()
        
        return {'label':'Fc', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#5a82ca', 'linestyle':'solid'}
    
    @property
    def fimag(self):
        nyq_rf = self.fs_rf/2
        fc = self.fc
        nco = self.nco
        
        ax_x = (2*nyq_rf - (fc+nco)) if (np.floor((fc+nco)/nyq_rf)%2 == 0) else (nyq_rf - ((fc+nco)%nyq_rf))
        ax_y = self.__get_freq_resp()
        
        return {'label':'Fc Image', 'x':ax_x, 'ymin':self.noisefloor, 'ymax':ax_y, 'color':'#c46728', 'linestyle':'solid'}
       
    @property
    def mix_mode(self):
        if self.fc > (self.fs_rf/2):
            return "Mix Mode: ON"
        else:
            return "Mix Mode: OFF"
    
    @property
    def effective_fs(self):
        return self.fs_rf/self.interp_rate
