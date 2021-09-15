import numpy as np

def arrayResponse(phi,theta,N):
    rps = np.zeros([1,N],dtype="complex")
    arrayWidth = np.int(np.sqrt(N))
    print(arrayWidth)
    for m in range(arrayWidth):
        for n in range(arrayWidth):
            #y(m * (sqrt(N)) + n + 1) = exp(1
            elementRps = np.exp(complex(0,np.pi*(m * np.sin(phi) * np.sin(theta) + n * np.cos(theta))))
            rps[0][m*arrayWidth+n] = elementRps
            pass
        pass
    rps = rps.transpose()/np.sqrt(N)
    return rps

def channel(at_phi,at_theta,ar_phi,ar_theta,Nt, Nr):
    at = arrayResponse(at_phi,at_theta,Nt)
    ar = arrayResponse(ar_phi,ar_theta,Nr)
    response = np.sqrt(Nr*Nt) * ar* at.transpose()
    return response

#多径叠加
def generateChannel(L,Nt,Nr):
    subPaths = []
    for i in range(L):
        aod = np.array([np.random.random(), np.random.random()]) * np.pi - np.pi / 2  # 出发角
        aoa = np.array([np.random.random(), np.random.random()]) * np.pi - np.pi / 2  # 到达角
        subPath = channel(aod[0],aod[1],aoa[0],aoa[1],Nt,Nr)
        subPaths.append(subPath)
        pass
    subPaths = np.array(subPaths)
    H = np.zeros(subPaths[0].shape)
    for i in subPaths:
        H = H+i/L
        pass
    return H



