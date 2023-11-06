'''
프로젝트 V-Fit 변경 사항 문서
=============================
이 문서는 프로젝트 V-Fit의 변경 사항을 문서화하고, Apache 2.0 라이선스에 따라 라이선스 정보와 고지 사항을 제공합니다.

변경 사항
-----------
1. 변경 사항 목적 및 이유:
   - 모듈 경로를 변경하여 코드 구성을 향상시키고 가독성을 개선하였습니다.

2. 변경된 파일 및 경로:
   - 변경 전: `from model import U2NET`
   - 변경 후: `from U2Net.model import U2NET`

   - 변경 전: `from model import U2NETP`
   - 변경 후: `from U2Net.model import U2NETP`
   
라이선스 정보
--------------
프로젝트 V-Fit는 Apache 2.0 라이선스 하에 배포됩니다. Apache 2.0 라이선스의 전체 텍스트는 "LICENSE" 파일에서 확인할 수 있습니다.
변경 사항은 Apache 2.0 라이선스에 따라 배포됩니다.
'''

import os
import torch
from U2Net.model import U2NET # full size version 173.6 MB
from U2Net.model import U2NETP # small version u2net 4.7 MB


def model(model_name='u2net'):


    model_dir = os.path.join(os.getcwd(), 'U2Net/saved_models', model_name, model_name + '.pth')

    if(model_name=='u2net'):
        print("...load U2NET---173.6 MB")
        net = U2NET(3,1)
    elif(model_name=='u2netp'):
        print("...load U2NEP---4.7 MB")
        net = U2NETP(3,1)
    net.load_state_dict(torch.load(model_dir))

    if torch.cuda.is_available():
        net.cuda()
    net.eval()

    return net
