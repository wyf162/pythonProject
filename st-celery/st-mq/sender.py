# _*_ coding: utf-8 _*_
# @Time : 2022/1/15 下午7:10 
# @Author : wangyefei
# @File : sender.py
import time

import rabbitpy


if __name__ == '__main__':
    with rabbitpy.Connection() as connnetion:
        with connnetion.channel() as channel:
            exchange = rabbitpy.Exchange(channel, 'chapter2-example', exchange_type='fanout')
            exchange.declare()

            queue = rabbitpy.Queue(channel, 'example')
            queue.declare()

            queue_yefe = rabbitpy.Queue(channel, 'yefe')
            queue_yefe.declare()
            queue.bind(exchange, 'example-routing-key')
            queue_yefe.bind(exchange, 'example-routing-key')

            num = 1

            while num<10:
                message = rabbitpy.Message(channel,
                                           f"Test message {num}",
                                           {"content_type": "application/json"},
                                           opinionated=True)
                message.publish(exchange, 'example-routing-key')
                time.sleep(2)
                num += 1
            