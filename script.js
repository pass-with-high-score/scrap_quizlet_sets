const quizLink = `
 // sample
`.trim()

const userRaw = `
fa835f1d-68e8-4e73-844e-84d38f87c6a1,
309e1815-dab4-40b5-a81a-096146b2f363,
bea1e8b6-8885-4f1d-a390-50df44a5b231,
57c0f580-9cc6-43ee-abcb-fb547ed5d14e,
6d4ec8b8-4af1-4b92-bd88-3a20b705bbea,
ace55a0c-24b8-4380-b92b-a9ecd613acd4,
51792e49-d461-4666-93bd-afa284a10d6f,
852bcd4f-40b2-48d2-9cdd-a46f17ba8b1d,
a1b235b8-1529-4168-b7c4-e5042dc8ba74,
7db05ffb-cc4f-4202-967b-63a50dc7effb,
2e7e8691-6101-4a4a-a9d6-db5e69e40f56,
43a0bd61-6d3f-4d46-b63c-d0d27035c36a,
1ec3107c-e275-45ff-8729-1586fbb9a561,
31913dea-723a-49a6-9362-89f65d8da836,
e1d8f71b-9788-41bc-973e-ba6974c9b5cc,
a089e108-f269-4468-9afd-453bcf7446da,
888deba5-0497-41fc-9eb9-b9d91ea697ad,
879757f9-a67c-406c-8a00-aef73daf57d9,
e48c4ae9-0147-4b69-9a55-43651027e1cf,
b757479e-4182-4461-8691-ae55a85429e8,
ecccb2ae-ad36-48fb-8369-1984a71e4a1b,
1e65d9e7-9354-4882-9326-8a56c4b98480,
b3a6f451-39bd-4804-a24e-b328bf4ff787,
500a6266-fa52-4147-817b-d3a90632fd7c,
33f1e773-1c70-403f-b054-306e35bef18b,
552a0875-34a7-4b8b-8203-4518f14777b1
`.trim()

function processLinks(links) {
    const rawLinks = links.trim().split('\n');

    const uniqueLinks = new Set();

    rawLinks.forEach(link => {
        uniqueLinks.add(link.trim() + ';');
    });

    return Array.from(uniqueLinks).join('\n');
}


const links = quizLink.trim().split(";\n").map(link => link.trim()).filter(link => link);
const userIds = userRaw.trim().split(",\n").map(userId => userId.trim()).filter(userId => userId);

const pairs = [];

userIds.forEach(userId => {
    links.forEach(link => {
        pairs.push({userId, link});
    });
});

console.log(pairs);
const jsonContent = JSON.stringify(pairs, null, 2);

const blob = new Blob([jsonContent], {type: 'application/json'});
const link = document.createElement('a');
link.href = URL.createObjectURL(blob);
link.download = 'user-quiz-links.json';
link.click();

// const processedLinks = processLinks(rawData);
// console.log(processedLinks);
