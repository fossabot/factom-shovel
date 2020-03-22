import os
import json
import unittest
import ptflow
from ptflow.storage.pgsql import Storage


if __name__ == '__main__':

        ptflow.initialize(Storage)
        m = ptflow.eventstore('octoe')

        def x_fail(action):
            res = m(action, roles=['*'], payload={'foo': 'bar'})
            #print(action, res)

        def x_pass(action):
            res = m(action, roles=['*'])
            #print(self.m.event(res[0]))
            #print(action, res)
            #print(self.m.state())

        x_fail('OFF')
        x_fail('EXEC')
        x_pass('ON')
        x_pass('EXEC')

        import IPython ; IPython.embed()
