# MainFrame 类代码完全是用wxformbuilder产生的。
# 不去动它

###########################################################################
## Python code generated with wxFormBuilder (version Mar  7 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
# import wx.xrc
import wx.grid


###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"API 测试工具", pos=wx.DefaultPosition, size=wx.Size(923, 611),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        choosebox_methodChoices = [u"GET", u"POST", u"PUT", u"DELETE"]
        self.choosebox_method = wx.ComboBox(self, wx.ID_ANY, u"POST", wx.DefaultPosition, wx.DefaultSize,
                                            choosebox_methodChoices, wx.CB_READONLY)
        self.choosebox_method.SetSelection(0)
        bSizer2.Add(self.choosebox_method, 1, wx.ALL | wx.EXPAND, 5)

        self.textctrl_url = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.textctrl_url, 4, wx.ALL | wx.EXPAND, 5)

        self.button_send = wx.Button(self, wx.ID_ANY, u"发送消息", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.button_send, 1, wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.ALL | wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer1.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"HTTP 消息头", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer6.Add(self.m_staticText2, 1, wx.ALL, 5)

        self.grid_headers = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_headers.CreateGrid(4, 2)
        self.grid_headers.EnableEditing(True)
        self.grid_headers.EnableGridLines(True)
        self.grid_headers.EnableDragGridSize(False)
        self.grid_headers.SetMargins(0, 0)

        # Columns
        self.grid_headers.SetColSize(0, 124)
        self.grid_headers.SetColSize(1, 159)
        self.grid_headers.EnableDragColMove(False)
        self.grid_headers.EnableDragColSize(True)
        self.grid_headers.SetColLabelSize(30)
        self.grid_headers.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_headers.EnableDragRowSize(True)
        self.grid_headers.SetRowLabelSize(80)
        self.grid_headers.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_headers.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer6.Add(self.grid_headers, 10, wx.ALL | wx.EXPAND, 5)

        bSizer3.Add(bSizer6, 3, wx.EXPAND, 5)

        self.m_staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL)
        bSizer3.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer61 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"HTTP 消息体", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer61.Add(self.m_staticText3, 2, wx.ALL, 5)

        self.checkbox_body_urlencode = wx.CheckBox(self, wx.ID_ANY, u"form-urlencoded格式", wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        self.checkbox_body_urlencode.SetValue(True)
        bSizer61.Add(self.checkbox_body_urlencode, 4, wx.ALL, 5)

        bSizer7.Add(bSizer61, 1, wx.EXPAND, 5)

        self.grid_body = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.grid_body.CreateGrid(4, 2)
        self.grid_body.EnableEditing(True)
        self.grid_body.EnableGridLines(True)
        self.grid_body.EnableDragGridSize(False)
        self.grid_body.SetMargins(0, 0)

        # Columns
        self.grid_body.SetColSize(0, 138)
        self.grid_body.SetColSize(1, 277)
        self.grid_body.EnableDragColMove(False)
        self.grid_body.EnableDragColSize(True)
        self.grid_body.SetColLabelSize(30)
        self.grid_body.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.grid_body.EnableDragRowSize(True)
        self.grid_body.SetRowLabelSize(80)
        self.grid_body.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.grid_body.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer7.Add(self.grid_body, 5, wx.ALL | wx.EXPAND, 5)

        self.textctrl_body = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.HSCROLL | wx.TE_MULTILINE)
        bSizer7.Add(self.textctrl_body, 5, wx.ALL | wx.EXPAND, 5)

        bSizer3.Add(bSizer7, 4, wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 5, wx.ALL | wx.EXPAND, 5)

        self.textctrl_msg_log = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                            wx.HSCROLL | wx.TE_MULTILINE)
        bSizer1.Add(self.textctrl_msg_log, 6, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button_send.Bind(wx.EVT_BUTTON, self.sendrequest)
        self.grid_headers.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.headerGridDClick)
        self.checkbox_body_urlencode.Bind(wx.EVT_CHECKBOX, self.setBodyUrlEncoded)
        self.grid_body.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.bodyGridDClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def sendrequest(self, event):
        event.Skip()

    def headerGridDClick(self, event):
        event.Skip()

    def setBodyUrlEncoded(self, event):
        event.Skip()

    def bodyGridDClick(self, event):
        event.Skip()




# 下面是我们自己的代码


# 定义自己的类继承自 wxformbuilder 自动生成的frame类
# 将我们的代码和  wxformbuilder 自动生成的代码 分离
# 这样当 wxformbuilder 自动生成的frame类 改变时，方便替换


import requests

class MyFrame(MainFrame):

    def __init__(self, parent):
        MainFrame.__init__(self,parent)
        self.setBodyUrlEncodedState()



    def setBodyUrlEncoded(self, event):
        self.setBodyUrlEncodedState()

    def setBodyUrlEncodedState(self):
        if self.checkbox_body_urlencode.IsChecked():
            self.grid_body.Enable()
            self.textctrl_body.Disable()
        else:
            self.grid_body.Disable()
            self.textctrl_body.Enable()


    def pretty_print_request(self,req):

        if req.body == None:
            msgBody = ''
        else:
            msgBody = req.body

        self.textctrl_msg_log.write(
            '{}\n{}\n{}\n\n{}'.format(
            '\n\n----------- 发送请求 -----------',
            req.method + ' ' + req.url,
            '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            msgBody,
        ))



    def pretty_print_response(self,res):
        self.textctrl_msg_log.write(
            '{}\nHTTP/1.1 {}\n{}\n\n{}'.format(
            '\n\n----------- 得到响应 -----------',
            res.status_code,
            '\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()),
            res.content.decode(),
        ))

    # 如果双击表格，看看是否是最后一行，如果是，添加一行
    def headerGridDClick(self, event):
        if self.grid_headers.GetNumberRows() == event.GetRow()+1:
            self.grid_headers.AppendRows()




    def bodyGridDClick(self, event):
        if self.grid_body.GetNumberRows() == event.GetRow()+1:
            self.grid_body.AppendRows()


    def sendrequest(self, event):

        # 获取请求方法
        method = self.choosebox_method.GetStringSelection()

        # 获取url
        url    = self.textctrl_url.GetValue()
        # 如果 url 不是以 http 或者https 开头，加上
        if not url.startswith('http://')  and not url.startswith('https://'):
            url = f'http://{url}'

        # 获取消息头
        headers = {}
        gh = self.grid_headers
        rowNumber = gh.GetNumberRows()
        for r in range(rowNumber):
            k = gh.GetCellValue(r,0)
            v = gh.GetCellValue(r,1)
            if k.strip() == '':
                continue
            headers[k] = v

        # print(headers)


        # 获取消息体
        isBodyUrlEncoded = self.checkbox_body_urlencode.IsChecked()

        # 如果消息体格式是 urlencoded，组合参数
        if isBodyUrlEncoded:
            payload = {}
            gb = self.grid_body
            rowNumber = gb.GetNumberRows()
            for r in range(rowNumber):
                k = gb.GetCellValue(r,0)
                v = gb.GetCellValue(r,1)
                if k.strip() == '':
                    continue
                payload[k] = v

        # 否则直接使用文本框里的内容作为消息体
        else:
            payload =self.textctrl_body.GetValue()


        req = requests.Request(method,
                               url,
                               headers=headers,
                               data=payload
                               )

        prepared = req.prepare()

        self.pretty_print_request(prepared)
        s = requests.Session()
        r = s.send(prepared)

        self.pretty_print_response(r)


app = wx.App(False)
frame = MyFrame(None)
frame.Show()
app.MainLoop()