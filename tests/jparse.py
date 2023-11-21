import json
import re
res = """
 Here is my attempt at an extract from the transcript:

{
  "clips": [
    {
      "start":"1:53:53.320",
      "end": "1:54:57.720",
      "title": "Does humanity still have primal tendencies?",
      "reason": "Discussion of how technology may help overcome biological limitations",
      "hashtags": ["technology","biology","limitations","evolution","humanity"]
    }
  ]
}

I chose this excerpt as it discusses an intriguing idea - that through technology like AI and neural interfaces, humanity may be able to edit out primal tendencies like jealousy, anxiety, etc. that are detrimental but were important for survival in the past. I thought it raised an interesting philosophical point about human evolution and limitations in a thought-provoking way. Please let me know if this extract meets the criteria or if you would like me to try again with a different selection."""

parsed = re.match(r".*?({.*}).*", res, re.DOTALL).group(1)
print(parsed)
data = json.loads(parsed)
items = data["clips"]

print(items)
