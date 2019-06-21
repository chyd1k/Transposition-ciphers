from PyQt5 import QtWidgets
import transp_ciphers_interface

class mainWindowApp(QtWidgets.QMainWindow,
                    transp_ciphers_interface.Ui_MainWindow):
    """This class implements main window of the application
    """
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.mode = 1
        self.res_Browser.setText('The key is the string!')
        self.sp1 = [
        ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
        '.', '/', '0',  '1',  '2',  '3',  '4',  '5',  '6',  '7',  '8',  '9',
        ':', ';', '<', '=', '>', '?'
        ]
        self.sp2 = [
        '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
        '\\', ']', '^', '_'
        ]
        self.sp3 = [
        '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{',
        '|', '}', '~'
        ]

        self.encrypt_Button.clicked.connect(self.encrypt)
        self.decrypt_Button.clicked.connect(self.decrypt)

        self.Vigenere_radioButton.clicked.connect(self.Vigenere_mode)
        self.Scytale_radioButton.clicked.connect(self.Scytale_mode)
        self.RailF_radioButton.clicked.connect(self.RailF_mode)
        self.VertT_radioButton.clicked.connect(self.VertT_mode)
        self.DoubleT_radioButton.clicked.connect(self.DoubleT_mode)

    def Vigenere_mode(self):
        self.mode = 1
        self.res_Browser.setText('The key is the string!')

    def Scytale_mode(self):
        self.mode = 2
        self.res_Browser.setText('The key is the rows amount!')

    def RailF_mode(self):
        self.mode = 3
        self.res_Browser.setText('The key is the rails count!')

    def VertT_mode(self):
        self.mode = 4
        self.res_Browser.setText('The key is the number of columns,' +
        ' press "Enter" and list them in the desired order.')

    def DoubleT_mode(self):
        self.mode = 5
        self.res_Browser.setText('The key is the two lists of numbers.' +
        'Each list express strings and columns transposition order.')

    def encrypt(self):
        message = self.mes_Browser.toPlainText()
        if self.mode == 1:
            key = self.key_Browser.toPlainText()
            enc_mes = self.Vigenere_enc(message, key)
            self.res_Browser.setText(enc_mes)
        elif self.mode == 2:
            key = int(self.key_Browser.toPlainText())
            enc_mes = self.Scytale_enc(message, key)
            self.res_Browser.setText(enc_mes)
        elif self.mode == 3:
            key = int(self.key_Browser.toPlainText())
            enc_mes = self.RailFence_enc(message, key)
            self.res_Browser.setText(enc_mes)
        elif self.mode == 4:
            data = self.key_Browser.toPlainText().split('\n')
            columns_amount = int(data[0])
            key = [int(i) for i in data[1].split(', ')]
            enc_mes = self.VTransp_enc(message, columns_amount, key)
            self.res_Browser.setText(enc_mes)
        elif self.mode == 5:
            data = self.key_Browser.toPlainText().split('\n')
            v_key = [int(i) for i in data[0].split(', ')]
            h_key = [int(i) for i in data[1].split(', ')]
            while len(message) % len(v_key) != 0:
                message += ' '
            if int(len(message) / len(v_key)) == len(h_key):
                enc_mes = self.DoubleT_enc(message, v_key, h_key)
                self.res_Browser.setText(enc_mes)
            else:
                self.res_Browser.append('The dimension of your second key ' +
                f'must be {int(len(message)/len(v_key))}.')

    def decrypt(self):
        message = self.encmes_Browser.toPlainText()
        if self.mode == 1:
            key = self.key_Browser.toPlainText()
            dec_mes = self.Vigenere_dec(message, key)
            self.res_Browser.setText(dec_mes)
        elif self.mode == 2:
            key = int(self.key_Browser.toPlainText())
            dec_mes = self.Scytale_dec(message, key)
            self.res_Browser.setText(dec_mes)
        elif self.mode == 3:
            key = int(self.key_Browser.toPlainText())
            dec_mes = self.RailFence_dec(message, key)
            self.res_Browser.setText(dec_mes)
        elif self.mode == 4:
            data = self.key_Browser.toPlainText().split('\n')
            columns_amount = int(data[0])
            key = [int(i) for i in data[1].split(', ')]
            dec_mes = self.VTransp_dec(message, columns_amount, key)
            self.res_Browser.setText(dec_mes)
        elif self.mode == 5:
            data = self.key_Browser.toPlainText().split('\n')
            v_key = [int(i) for i in data[0].split(', ')]
            h_key = [int(i) for i in data[1].split(', ')]
            while len(message) % len(v_key) != 0:
                message += ' '
            if int(len(message)/len(v_key)) == len(h_key):
                dec_mes = self.DoubleT_dec(message, v_key, h_key)
                self.res_Browser.setText(dec_mes)
            else:
                self.res_Browser.append('The dimension of your second key ' +
                f'must be {int(len(message)/len(v_key))}.')

    def Vigenere_enc(self, mes, key):
        key *= (len(mes) // len(key)) + 1
        enc_mes, mes = '', list(mes)
        for i in range(len(mes)):
            if mes[i] in self.sp1:
                temp = ord(mes[i]) + ord(key[i])
                enc_mes += chr(temp % 32 + ord(' '))
            elif mes[i] in self.sp2:
                temp = ord(mes[i]) + ord(key[i])
                enc_mes += chr(temp % 32 + ord('@'))
            elif mes[i] in self.sp3:
                temp = ord(mes[i]) + ord(key[i])
                enc_mes += chr(temp % 32 + ord('`'))
        return enc_mes

    def Vigenere_dec(self, enc_mes, key):
        key *= (len(enc_mes) // len(key)) + 1
        dec_mes, enc_mes = '', list(enc_mes)
        for i in range(len(enc_mes)):
            if enc_mes[i] in self.sp1:
                temp = ord(enc_mes[i]) - ord(key[i])
                dec_mes += chr(temp % 32 + ord(' '))
            elif enc_mes[i] in self.sp2:
                temp = ord(enc_mes[i]) - ord(key[i])
                dec_mes += chr(temp % 64 + ord('@'))
            elif enc_mes[i] in self.sp3:
                temp = ord(enc_mes[i]) - ord(key[i])
                dec_mes += chr(temp % 32 + ord('`'))
        return dec_mes

    def Scytale_enc(self, mes, rows_amount):
        while len(mes) % rows_amount != 0:
            mes += ' '
        columns_amount, mes = int(len(mes) / rows_amount), list(mes)
        enc_mes = [mes[i : i + columns_amount] for i in range (0, len(mes), columns_amount)]
        res = []
        [[res.append(enc_mes[j][i]) for j in range(len(enc_mes))] for i in range(len(enc_mes[0]))]
        res = ''.join(res)
        return res

    def Scytale_dec(self, enc_mes, rows_amount):
        columns_amount = int(len(enc_mes) / rows_amount)
        dec_mes = self.Scytale_enc(enc_mes, columns_amount)
        return dec_mes

    def RailFence_enc(self, mes, key):
            enc_mes = []
            matrix = [['' for x in range(len(mes))] for y in range(key)]
            inc, row, col = 1, 0, 0
            for i in mes:
                    if row + inc < 0 or row + inc >= len(matrix):
                            inc = inc * (-1)
                    matrix[row][col] = i
                    row += inc
                    col += 1
            [enc_mes.append(''.join(list)) for list in matrix]
            enc_mes = ''.join(enc_mes)
            return enc_mes

    def RailFence_dec(self, enc_mes, key):
            dec_mes = []
            matrix = [['' for x in range(len(enc_mes))] for y in range(key)]
            idx, inc = 0, 1
            for selectedRow in range(len(matrix)):
                    row = 0
                    for col in range(0, len(matrix[row])):
                            if row + inc < 0 or row + inc >= len(matrix):
                                    inc = inc * (-1)
                            if row == selectedRow:
                                    matrix[row][col] += enc_mes[idx]
                                    idx += 1
                            row += inc
            [dec_mes.append(''.join(list)) for list in self.transpose(matrix)]
            dec_mes = ''.join(dec_mes)
            return dec_mes

    def transpose(self, m):
        #Getting a transposed matrix (replacing rows with columns)
    	transp = [[0 for y in range(len(m))] for x in range(len(m[0]))]
    	for i in range(len(m)):
    		for j in range(len(m[0])):
    			transp[j][i] = m[i][j]
    	return transp

    def VTransp_enc(self, mes, columns_amount, key):
        while len(mes) % columns_amount != 0:
            mes += ' '
        rows_amount = int(len(mes) / columns_amount)
        temp, x, enc_mes = [], [], []
        [[temp.append(mes[i]) for i in range (j, len(mes), columns_amount)] for j in range(columns_amount)]
        temp = ''.join(temp)
        x = [temp[i : i + rows_amount] for i in range (0, len(temp), rows_amount)]
        enc_mes = [x[i - 1] for i in key]
        enc_mes = ''.join(enc_mes)
        return enc_mes

    def VTransp_dec(self, enc_mes, columns_amount, key):
        while len(enc_mes) % columns_amount != 0:
            enc_mes += ' '
        rows_amount = int(len(enc_mes) / columns_amount)
        x = [enc_mes[i : i + rows_amount] for i in range (0, len(enc_mes), rows_amount)]
        s = [None for i in range(columns_amount)]
        for bl, num in zip(x, key):
            s[num - 1] = bl
        s = ''.join(s)
        dec_mes = []
        [[dec_mes.append(s[i]) for i in range (j, len(s), rows_amount)] for j in range(rows_amount)]
        dec_mes = ''.join(dec_mes)
        return dec_mes

    def DoubleT_enc(self, mes, v_key, h_key):
    	enc_mes = [mes[i : i + len(v_key)] for i in range (0, len(mes), len(v_key))]
    	#Vertical transposition
    	temp = {}
    	for i in range(len(v_key)):
    		temp[v_key[i]] = [item[i] for item in enc_mes]
    	#Horizontal transposition
    	enc_mes = {}
    	for i in range(len(h_key)):
    		enc_mes[h_key[i]] = [temp[key][i] for key in sorted(temp)]
    	res = ''
    	for i in range(len(h_key)):
    		res += ''.join(enc_mes[i + 1])
    	return res

    def DoubleT_dec(self, enc_mes, v_key, h_key):
    	enc_mes = [enc_mes[i : i + len(v_key)] for i in range (0, len(enc_mes), len(v_key))]
    	#Horizontal transposition
    	temp = {}
    	for i in range(len(h_key)):
    		temp[h_key[i]] = enc_mes[h_key[i] - 1]
    	#Vertical transposition
    	x = [temp[i] for i in h_key]
    	temp = {}
    	for i in range(len(v_key)):
    		temp[i + 1] = [item[i] for item in x]
    	dec_mes = ''
    	for i in range(len(h_key)):
    		for key in v_key:
    			dec_mes += temp[key][i]
    	return dec_mes


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindowApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
