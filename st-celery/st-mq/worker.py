5# _*_ coding: utf-8 _*_
# @Time : 2022/1/15 下午8:09 
# @Author : wangyefei
# @File : worker.py


import rabbitpy

if __name__ == '__main__':

    with rabbitpy.Connection('amqp://guest:guest@localhost:5672/%2f') as conn:
        print(conn.args)
        print(conn.capabilities)
        print(conn.server_properties)
        with conn.channel() as channel:
            queue = rabbitpy.Queue(channel, 'yefe')
            while len(queue) > 0:
                message = queue.get()
                message.pprint(True)
                message.ack()
                print('There are {} more messages in the queue'.format(len(queue)))
