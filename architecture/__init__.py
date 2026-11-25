def model_generator(method, opt=None):
    
    if method=='hyper':
        if opt.stage==3:
            from .HyperBMU import HyperBMU

           
        model = HyperBMU(opt).cuda()  
    else:
        print(f'Method {method} is not defined !!!!')

    return model


