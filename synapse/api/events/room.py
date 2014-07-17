# -*- coding: utf-8 -*-
from . import SynapseEvent


class RoomTopicEvent(SynapseEvent):

    def get_content_template(self):
        return {"topic": u"string"}


class MessageEvent(SynapseEvent):

    def __init__(self, content, pdu=None, **kwargs):
        super(MessageEvent, self).__init__(content)
        if not pdu:
            self.room_id = kwargs["room_id"]
            self.user_id = kwargs["user_id"]
            self.msg_id = kwargs["msg_id"]
        else:
            pass  # TODO pdu impl

    def get_content_template(self):
        return {"msgtype": u"string"}