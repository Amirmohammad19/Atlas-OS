import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from router import MessageRouter


router = MessageRouter()


response = router.process(
    1,
    "Hello Atlas"
)


print(response)