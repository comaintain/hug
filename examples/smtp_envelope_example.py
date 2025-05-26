import envelopes
import hug


@hug.directive()
class SMTP:
    def __init__(self, *args, **kwargs):
        self.smtp = envelopes.SMTP(host="127.0.0.1")
        self.envelopes_to_send = list()

    def send_envelope(self, envelope):
        self.envelopes_to_send.append(envelope)

    def cleanup(self, exception=None):
        if exception:
            return
        for envelope in self.envelopes_to_send:
            self.smtp.send(envelope)


@hug.get("/hello")
def send_hello_email(smtp: SMTP):
    envelope = envelopes.Envelope(
        from_addr=("me@example.com", "From me"),
        to_addr=("world@example.com", "To World"),
        subject="Hello",
        text_body="World!",
    )
    smtp.send_envelope(envelope)
