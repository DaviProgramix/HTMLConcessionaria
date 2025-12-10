import speedtest

teste = speedtest.Speedtest()

# Teste Do Download : 
print("Testando Download")
velocidade_download = teste.download()
print(f"Velocidade de Download : {velocidade_download / 10**6: .2f}")

# Teste Do Upload : 
print("Testando Upload")
velocidade_upload = teste.upload()
print(f"Velocidade de Upload : {velocidade_upload / 10**6: .2f}")

# Teste Do Ping : 
ping = teste.results.ping
print(f"Ping : {ping: .2f}")