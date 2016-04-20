import logging
import mido

logger = logging.getLogger(__name__)

class BaseHandler():
    def handle_msg(self, msg, *args, **kwargs):
        '''
        Trys to handle a mido message
        '''
        try:
            handler_name = '_{}_handler'.format(msg.type)
            if hasattr(self, handler_name):
                handler = getattr(self, handler_name, default=self._handler_not_implemented)
                return handler(msg, *args, **kwargs)

        except:
            return None
