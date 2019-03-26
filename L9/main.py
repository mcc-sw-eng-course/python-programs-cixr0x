
import tictac
import tictac_client
import tictac_server
import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if (len(sys.argv) >= 2):
    mode = sys.argv[1]
    #ip = sys.argv[2]
    if (mode=="client"):
        tt=tictac_client.Tictac()
    elif (mode == "server"):
        tt =tictac_server.Tictac()
else:
    tt = tictac.Tictac()
    
tt.main_loop()