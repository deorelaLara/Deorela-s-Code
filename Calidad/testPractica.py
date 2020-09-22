import unittest
from practica import getHorario
#########################################################
class RepoMock():
    def __init__(self):
        self.goodAdmin = []
        self.Horarios = {}
    
    def IsAdmin(self, admin):
        if admin in self.goodAdmin:
            return True

        return False
    
    def GetHorario(self, mat):
        if mat in self.Horarios:
            return self.Horarios[mat]
        return ""
    
    def setAdmin(self, admin):
        self.goodAdmin.append(admin)
    
    def setHorario(self, mat, horario):
        self.Horarios[mat] = horario
########################################################
class TestPractica(unittest.TestCase):
    def test_getHorario(self):
        tts = [
            {'req_user': "1995",
            'mat': "1234",
            'exp_out': 'Lunes 16:00 Algoritmos',
            'good_users': ["0000", '1234', '2222','1995']
            },
            {'req_user': "9999",
            'mat': "1234",
            'exp_out': 'ERROR 404',
            'good_users': ["0000", '2222','9999'],
            },
            {'req_user': "1995",
            'mat': "10021265",
            'exp_out': 'ERROR 404',
            'good_users': ["0000", '2222','1995'],
            }
        ] 

        for tc in tts:
            mock = RepoMock()
            for admin in tc['good_users']:
                mock.setAdmin(admin)
            mock.setHorario(tc['mat'], tc['exp_out'])
            salida = getHorario(tc['req_user'], tc['mat'], mock)
            self.assertEqual(salida, tc['exp_out'])

if __name__ == "__main__":
    unittest.main()