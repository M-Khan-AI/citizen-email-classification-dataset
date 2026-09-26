# Email Classification – Evaluation Report

Dataset size: **200** labeled emails

## Overall Accuracy

| Stage | Accuracy |
|---|---|
| Model only (raw `classify_email()` output) | 10.5% |
| Model + keyword fallback | 90.5% |

⚠️ Below the 70% target — see notes below.

## Per-Category Metrics (model only, before fallback)

| Category | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Complaint | 1.00 | 0.04 | 0.08 | 50 |
| General Info | 0.75 | 0.12 | 0.21 | 50 |
| Missed Pickup | 1.00 | 0.12 | 0.21 | 50 |
| Schedule Change | 1.00 | 0.14 | 0.25 | 50 |

## Per-Category Metrics (after keyword fallback)

| Category | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Complaint | 0.96 | 0.96 | 0.96 | 50 |
| General Info | 0.94 | 0.66 | 0.78 | 50 |
| Missed Pickup | 1.00 | 1.00 | 1.00 | 50 |
| Schedule Change | 0.96 | 1.00 | 0.98 | 50 |

## Cases Returned as 'Uncertain' by the Model

Total: **177** out of 200 emails.

| True Label | Email (truncated) |
|---|---|
| Complaint | Hello, I would like to complain about the overflowing public bin near 17 Green Park Road. It has not... |
| Missed Pickup | Hello, household rubbish at 8 Model Town Street were not collected on Wednesday, although this is ou... |
| Schedule Change | Good afternoon. Please clarify the collection schedule for 14 Civic Colony during the holiday period... |
| Complaint | Please log a Complaint about loose rubbish and broken glass left near 72 Mill Street. It is a hazard... |
| General Info | Can you tell me whether small cardboard boxes should go in the recycling bin or be taken to a drop-o... |
| Missed Pickup | Good afternoon. We brought the bins to the curb before 7 a.m. at 42 Central Avenue, but they are sti... |
| Schedule Change | Could you confirm whether the Friday collection for 36 Hill View Drive will move because of the publ... |
| Complaint | I am unhappy with the condition of the recycling point near 5 Orchard Lane. Cardboard and bottles ha... |
| General Info | Good morning. Can you tell me whether small cardboard boxes should go in the recycling bin or be tak... |
| Missed Pickup | Our collection was skipped this week at 17 Green Park Road. Neighbours on the next street seem to ha... |
| Schedule Change | We will be away during the usual collection day. Has the timetable for 28 Canal View changed this mo... |
| Complaint | Good afternoon. There is a strong smell coming from the waste containers near 31 Lake Road. The area... |
| Missed Pickup | Our collection was skipped this week at 61 North Street. Neighbours on the next street seem to have ... |
| Schedule Change | Hello, Please clarify the collection schedule for 23 Garden Block during the holiday period. Will th... |
| Complaint | A waste truck has repeatedly blocked the entrance near 42 Central Avenue while collecting bins. Coul... |
| General Info | What materials are accepted at the local recycling centre, and what are its opening hours?... |
| Missed Pickup | Good afternoon. I am reporting a missed pickup at 14 Civic Colony. The bins have been left outside s... |
| Schedule Change | I heard the refuse timetable may be different next week. What day should residents at 77 University ... |
| Complaint | I am unhappy with the condition of the recycling point near 28 Canal View. Cardboard and bottles hav... |
| General Info | Good morning. Is there a collection service for garden branches and leaves? If so, do they need to b... |
| Missed Pickup | The collection team passed 105 River Road without emptying our bin on Tuesday. It is now full, and l... |
| Schedule Change | We will be away during the usual collection day. Has the timetable for 23 Garden Block changed this ... |
| Complaint | Good morning. There is a strong smell coming from the waste containers near 66 New Garden Town. The ... |
| General Info | Could you explain how to report an abandoned shopping trolley or dumped item that is not in a househ... |
| Missed Pickup | Hello, our regular collection at 12 Sunrise Boulevard were not collected on Friday, although this is... |
| Schedule Change | Good afternoon. Please clarify the collection schedule for 31 Lake Road during the holiday period. W... |
| Complaint | Several bins near 9 Market Lane are overflowing even though they were emptied recently. Please check... |
| General Info | Please let me know how residents can request an extra rubbish bin for a larger household.... |
| Missed Pickup | Good afternoon. Hello, the kitchen-waste container at 9 Market Lane were not collected on Tuesday, a... |
| Schedule Change | I heard the refuse timetable may be different next week. What day should residents at 66 New Garden ... |
| Complaint | I would like to complain about the overflowing public bin near 47 Parkside Avenue. It has not been e... |
| General Info | Hello, Hello, where can I find the rules for sorting household waste and recycling? I want to make s... |
| Missed Pickup | Hello, the general waste bags at 53 Maple Street were not collected on Wednesday, although this is o... |
| Schedule Change | We will be away during the usual collection day. Has the timetable for 61 North Street changed this ... |
| Complaint | Hello, The collection crew left torn bags and scattered rubbish outside 36 Hill View Drive after emp... |
| General Info | Please let me know how residents can request an extra rubbish bin for a larger household.... |
| Missed Pickup | I am reporting a missed pickup at 23 Garden Block. The bins have been left outside since Friday morn... |
| Schedule Change | Good afternoon. Our regular collection falls on Wednesday. Is the service running as normal, or has ... |
| Complaint | Please log a Complaint about loose rubbish and broken glass left near 84 Railway Colony. It is a haz... |
| General Info | Can you tell me whether small cardboard boxes should go in the recycling bin or be taken to a drop-o... |
| Missed Pickup | Hello, Good afternoon. The scheduled refuse pickup at 14 Civic Colony did not happen today. Can this... |
| Schedule Change | We will be away during the usual collection day. Has the timetable for 28 Canal View changed this mo... |
| Complaint | I would like to complain about the overflowing public bin near 53 Maple Street. It has not been empt... |
| General Info | Good morning. What materials are accepted at the local recycling centre, and what are its opening ho... |
| Missed Pickup | I am reporting a missed pickup at 5 Orchard Lane. The bins have been left outside since Tuesday morn... |
| Schedule Change | I heard the refuse timetable may be different next week. What day should residents at 36 Hill View D... |
| Complaint | Hello, There is a strong smell coming from the waste containers near 84 Railway Colony. The area is ... |
| General Info | Is there a collection service for garden branches and leaves? If so, do they need to be tied into bu... |
| Missed Pickup | We brought the bins to the curb before 7 a.m. at 14 Civic Colony, but they are still full. Our norma... |
| Schedule Change | Good morning. We will be away during the usual collection day. Has the timetable for 8 Model Town St... |
| Complaint | The shared dumpster beside 36 Hill View Drive is damaged and its lid will not close. Animals are get... |
| General Info | Is there a collection service for garden branches and leaves? If so, do they need to be tied into bu... |
| Missed Pickup | Hello, I am reporting a missed pickup at 61 North Street. The bins have been left outside since Wedn... |
| Schedule Change | We will be away during the usual collection day. Has the timetable for 23 Garden Block changed this ... |
| Complaint | The shared dumpster beside 53 Maple Street is damaged and its lid will not close. Animals are gettin... |
| General Info | Hello, Where should used batteries and a small broken electronic appliance be taken for safe disposa... |
| Missed Pickup | The collection team passed 17 Green Park Road without emptying our bin on Monday. It is now full, an... |
| Schedule Change | Our regular collection falls on Saturday. Is the service running as normal, or has the route been re... |
| Complaint | Hello, Please log a complaint about loose rubbish and broken glass left near 53 Maple Street. It is ... |
| General Info | Hello, where can I find the rules for sorting household waste and recycling? I want to make sure I u... |
| Missed Pickup | Hello, the kitchen-waste container at 31 Lake Road were not collected on Saturday, although this is ... |
| Schedule Change | Good morning. The notice on the community board was unclear. Could you send the revised waste collec... |
| Complaint | I would like to complain about the overflowing public bin near 14 Civic Colony. It has not been empt... |
| General Info | I have an old mattress to dispose of. How do I book a bulky-waste collection, and are there any size... |
| Missed Pickup | Hello, We brought the bins to the curb before 7 a.m. at 14 Civic Colony, but they are still full. Ou... |
| General Info | Where should used batteries and a small broken electronic appliance be taken for safe disposal?... |
| Missed Pickup | Hello, household rubbish at 5 Orchard Lane were not collected on Friday, although this is our usual ... |
| Complaint | I am unhappy with the condition of the recycling point near 19 College Road. Cardboard and bottles h... |
| General Info | Could you explain how to report an abandoned shopping trolley or dumped item that is not in a househ... |
| Missed Pickup | Good afternoon. We brought the bins to the curb before 7 a.m. at 47 Parkside Avenue, but they are st... |
| Schedule Change | Could you confirm whether the Saturday collection for 12 Sunrise Boulevard will move because of the ... |
| Complaint | There is a strong smell coming from the waste containers near 14 Civic Colony. The area is attractin... |
| General Info | Good afternoon. Please let me know how residents can request an extra rubbish bin for a larger house... |
| Missed Pickup | I am reporting a missed pickup at 8 Model Town Street. The bins have been left outside since Saturda... |
| Schedule Change | Please clarify the collection schedule for 53 Maple Street during the holiday period. Will the usual... |
| Complaint | Good morning. Several bins near 53 Maple Street are overflowing even though they were emptied recent... |
| General Info | I have an old mattress to dispose of. How do I book a bulky-waste collection, and are there any size... |
| Missed Pickup | The collection team passed 12 Sunrise Boulevard without emptying our bin on Tuesday. It is now full,... |
| Schedule Change | Hello, Could you confirm whether the Tuesday collection for 23 Garden Block will move because of the... |
| Complaint | A waste truck has repeatedly blocked the entrance near 8 Model Town Street while collecting bins. Co... |
| General Info | Is there a collection service for garden branches and leaves? If so, do they need to be tied into bu... |
| Missed Pickup | Hello, Our collection was skipped this week at 19 College Road. Neighbours on the next street seem t... |
| Schedule Change | We will be away during the usual collection day. Has the timetable for 61 North Street changed this ... |
| Complaint | Several bins near 36 Hill View Drive are overflowing even though they were emptied recently. Please ... |
| General Info | Hello, What materials are accepted at the local recycling centre, and what are its opening hours?... |
| Missed Pickup | I am reporting a missed pickup at 61 North Street. The bins have been left outside since Thursday mo... |
| Schedule Change | We will be away during the usual collection day. Has the timetable for 47 Parkside Avenue changed th... |
| Complaint | Good morning. There is a strong smell coming from the waste containers near 42 Central Avenue. The a... |
| General Info | What materials are accepted at the local recycling centre, and what are its opening hours?... |
| Missed Pickup | I am reporting a missed pickup at 8 Model Town Street. The bins have been left outside since Wednesd... |
| Schedule Change | Good morning. Our regular collection falls on Wednesday. Is the service running as normal, or has th... |
| Complaint | I am unhappy with the condition of the recycling point near 28 Canal View. Cardboard and bottles hav... |
| General Info | Is there a collection service for garden branches and leaves? If so, do they need to be tied into bu... |
| Missed Pickup | Good morning. Hello, household rubbish at 84 Railway Colony were not collected on Wednesday, althoug... |
| Schedule Change | Could you confirm whether the Saturday collection for 42 Central Avenue will move because of the pub... |
| Complaint | A waste truck has repeatedly blocked the entrance near 36 Hill View Drive while collecting bins. Cou... |
| General Info | Good morning. Can you tell me whether small cardboard boxes should go in the recycling bin or be tak... |
| Missed Pickup | Hello, our refuse bins at 8 Model Town Street were not collected on Tuesday, although this is our us... |
| Complaint | Good afternoon. There is a strong smell coming from the waste containers near 23 Garden Block. The a... |
| General Info | Can you tell me whether small cardboard boxes should go in the recycling bin or be taken to a drop-o... |
| Missed Pickup | We brought the bins to the curb before 7 a.m. at 42 Central Avenue, but they are still full. Our nor... |
| Schedule Change | Good afternoon. Please clarify the collection schedule for 36 Hill View Drive during the holiday per... |
| Complaint | Several bins near 28 Canal View are overflowing even though they were emptied recently. Please check... |
| General Info | Please let me know how residents can request an extra rubbish bin for a larger household.... |
| Missed Pickup | Good morning. Hello, our regular collection at 12 Sunrise Boulevard were not collected on Friday, al... |
| Schedule Change | The notice on the community board was unclear. Could you send the revised waste collection dates for... |
| Complaint | Please log a complaint about loose rubbish and broken glass left near 84 Railway Colony. It is a haz... |
| General Info | Good afternoon. What materials are accepted at the local recycling centre, and what are its opening ... |
| Missed Pickup | We brought the bins to the curb before 7 a.m. at 105 River Road, but they are still full. Our normal... |
| Schedule Change | We will be away during the usual collection day. Has the timetable for 23 Garden Block changed this ... |
| Complaint | Good afternoon. The shared dumpster beside 42 Central Avenue is damaged and its lid will not close. ... |
| General Info | What materials are accepted at the local recycling centre, and what are its opening hours?... |
| Missed Pickup | I am reporting a missed pickup at 17 Green Park Road. The bins have been left outside since Monday m... |
| Schedule Change | Good afternoon. Our regular collection falls on Thursday. Is the service running as normal, or has t... |
| Complaint | Several bins near 9 Market Lane are overflowing even though they were emptied recently. Please check... |
| General Info | I have an old mattress to dispose of. How do I book a bulky-waste collection, and are there any size... |
| Missed Pickup | Hello, The collection team passed 23 Garden Block without emptying our bin on Monday. It is now full... |
| Schedule Change | The notice on the community board was unclear. Could you send the revised waste collection dates for... |
| Complaint | The collection crew left torn bags and scattered rubbish outside 61 North Street after emptying the ... |
| General Info | Good afternoon. Could you explain how to report an abandoned shopping trolley or dumped item that is... |
| Missed Pickup | We brought the bins to the curb before 7 a.m. at 8 Model Town Street, but they are still full. Our n... |
| Schedule Change | I heard the refuse timetable may be different next week. What day should residents at 12 Sunrise Bou... |
| Complaint | Good afternoon. The shared dumpster beside 42 Central Avenue is damaged and its lid will not close. ... |
| General Info | What materials are accepted at the local recycling centre, and what are its opening hours?... |
| Missed Pickup | We brought the bins to the curb before 7 a.m. at 9 Market Lane, but they are still full. Our normal ... |
| Schedule Change | Good afternoon. Please clarify the collection schedule for 31 Lake Road during the holiday period. W... |
| Complaint | The shared dumpster beside 19 College Road is damaged and its lid will not close. Animals are gettin... |
| General Info | What materials are accepted at the local recycling centre, and what are its opening hours?... |
| Missed Pickup | Good afternoon. Our collection was skipped this week at 28 Canal View. Neighbours on the next street... |
| Schedule Change | Our regular collection falls on Thursday. Is the service running as normal, or has the route been re... |
| Complaint | I would like to complain about the overflowing public bin near 31 Lake Road. It has not been emptied... |
| General Info | Good morning. Hello, where can I find the rules for sorting household waste and recycling? I want to... |
| Missed Pickup | The collection team passed 61 North Street without emptying our bin on Thursday. It is now full, and... |
| Schedule Change | Our regular collection falls on Tuesday. Is the service running as normal, or has the route been res... |
| Complaint | Hello, Please log a complaint about loose rubbish and broken glass left near 47 Parkside Avenue. It ... |
| Schedule Change | Our regular collection falls on Monday. Is the service running as normal, or has the route been resc... |
| Complaint | I would like to complain about the overflowing public bin near 31 Lake Road. It has not been emptied... |
| General Info | Good afternoon. What materials are accepted at the local recycling centre, and what are its opening ... |
| Missed Pickup | Hello, household rubbish at 8 Model Town Street were not collected on Saturday, although this is our... |
| Schedule Change | I heard the refuse timetable may be different next week. What day should residents at 84 Railway Col... |
| Complaint | Good afternoon. There is a strong smell coming from the waste containers near 42 Central Avenue. The... |
| General Info | Please let me know how residents can request an extra rubbish bin for a larger household.... |
| Missed Pickup | Good afternoon. The scheduled refuse pickup at 5 Orchard Lane did not happen today. Can this be logg... |
| Schedule Change | Good afternoon. Could you confirm whether the Friday collection for 72 Mill Street will move because... |
| Complaint | Several bins near 8 Model Town Street are overflowing even though they were emptied recently. Please... |
| General Info | Can you tell me whether small cardboard boxes should go in the recycling bin or be taken to a drop-o... |
| Missed Pickup | Hello, We brought the bins to the curb before 7 a.m. at 31 Lake Road, but they are still full. Our n... |
| Schedule Change | Could you confirm whether the Wednesday collection for 12 Sunrise Boulevard will move because of the... |
| Complaint | Several bins near 9 Market Lane are overflowing even though they were emptied recently. Please check... |
| General Info | Hello, I am moving into the area soon. Could you share the usual collection days and explain how to ... |
| Missed Pickup | The collection team passed 47 Parkside Avenue without emptying our bin on Thursday. It is now full, ... |
| Schedule Change | Our regular collection falls on Wednesday. Is the service running as normal, or has the route been r... |
| Complaint | Good afternoon. I am unhappy with the condition of the recycling point near 105 River Road. Cardboar... |
| General Info | Is there a collection service for garden branches and leaves? If so, do they need to be tied into bu... |
| Missed Pickup | I am reporting a missed pickup at 28 Canal View. The bins have been left outside since Wednesday mor... |
| Schedule Change | Good afternoon. Our regular collection falls on Monday. Is the service running as normal, or has the... |
| Complaint | A waste truck has repeatedly blocked the entrance near 61 North Street while collecting bins. Could ... |
| General Info | I am moving into the area soon. Could you share the usual collection days and explain how to request... |
| Schedule Change | Please clarify the collection schedule for 66 New Garden Town during the holiday period. Will the us... |
| Complaint | The shared dumpster beside 53 Maple Street is damaged and its lid will not close. Animals are gettin... |
| General Info | Good morning. Is there a collection service for garden branches and leaves? If so, do they need to b... |
| Missed Pickup | The collection team passed 61 North Street without emptying our bin on Tuesday. It is now full, and ... |
| Schedule Change | Could you confirm whether the Monday collection for 28 Canal View will move because of the public ho... |
| Complaint | Good afternoon. Several bins near 23 Garden Block are overflowing even though they were emptied rece... |
| General Info | Do you provide compost bins or guidance for starting home composting? Please point me to the relevan... |
| Missed Pickup | Good afternoon. The scheduled refuse pickup at 77 University Road did not happen today. Can this be ... |
| Schedule Change | Good morning. Please clarify the collection schedule for 19 College Road during the holiday period. ... |
| Complaint | I am unhappy with the condition of the recycling point near 23 Garden Block. Cardboard and bottles h... |
| General Info | What materials are accepted at the local recycling centre, and what are its opening hours?... |
| Missed Pickup | Good afternoon. Good afternoon. The scheduled refuse pickup at 31 Lake Road did not happen today. Ca... |
| Schedule Change | Our regular collection falls on Friday. Is the service running as normal, or has the route been resc... |
| Complaint | I am unhappy with the condition of the recycling point near 14 Civic Colony. Cardboard and bottles h... |
| General Info | Good morning. What materials are accepted at the local recycling centre, and what are its opening ho... |
| Missed Pickup | We brought the bins to the curb before 7 a.m. at 47 Parkside Avenue, but they are still full. Our no... |
| Schedule Change | Could you confirm whether the Saturday collection for 105 River Road will move because of the public... |
| Complaint | Good afternoon. The collection crew left torn bags and scattered rubbish outside 105 River Road afte... |
| General Info | Hello, where can I find the rules for sorting household waste and recycling? I want to make sure I u... |

## Fallback Logic

When `classify_email()` returns `"Uncertain"`, a simple keyword-matching function (`keyword_fallback()` in `fallback.py`) is applied as a second pass. It checks the email text (lowercased) against a short list of high-signal phrases per category — for example, `"did not come"` or `"missed pickup"` → **Missed Pickup**; `"overflowing"` or `"smell"` → **Complaint**; `"opening hours"` or `"how do i"` → **General Info**; `"timetable"` or `"reschedule"` → **Schedule Change**. The first matching category wins. If no keyword matches, the email stays `"Uncertain"`.

This fallback resolved **164** of the **177** Uncertain cases; **13** remained Uncertain after the fallback.

## Confusion Matrix (model only)

| True \ Predicted | Complaint | General Info | Missed Pickup | Schedule Change | Uncertain |
|---|---|---|---|---|---|
| Complaint | 2 | 2 | 0 | 0 | 46 |
| General Info | 0 | 6 | 0 | 0 | 44 |
| Missed Pickup | 0 | 0 | 6 | 0 | 44 |
| Schedule Change | 0 | 0 | 0 | 7 | 43 |
| Uncertain | 0 | 0 | 0 | 0 | 0 |
