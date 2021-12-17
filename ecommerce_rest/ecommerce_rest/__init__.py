import py_eureka_client.eureka_client as eureka_client


your_rest_server_port  =  8000
eureka_client.init(eureka_server = "http://localhost:8761/eureka/" ,
                                 app_name = "inventory" ,
                                 instance_port =(your_rest_server_port),
                                  )

