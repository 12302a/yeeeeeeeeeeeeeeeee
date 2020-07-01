import random
from discord import Member
from discord.ext import commands
from urllib.request import urlopen, Request
import urllib
import urllib.request
import os
import sys
import time
import datetime
import discord
import asyncio
import re

token = 'NzI2NzM4ODc1MTMyODA1MTUx.XvxAvA.eyz_OHKDDZebj3Zfde83XZGRXOY'
client = discord.Client()

@client.event
async def on_ready():
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')
    messages = [f'{len(client.guilds)}개의 서버 | {len(client.users)}명의 유저', "이 메세지는 10초마다 바뀝니다.", "https://www.twitch.tv/chaos_insurgency1 반란죄수님 프로필입니다!" ]
    while True:
       await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
       messages.append(messages.pop(0))
       await asyncio.sleep(10)  

@client.event
async def on_message(message):
    text = message.content
    if text == '반란죄수':
        await message.channel.send('엄청난 분')
    if text == '블랙리스트 지정':
        embed=discord.Embed(color=0xff00, title="오류발생", description="오류의 원인을 알 수 없습니다. @12302a 에게  해당 문제를 전송해주세요 :(", timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if text == '트위치':
        await message.channel.send('https://www.twitch.tv/chaos_insurgency1')
    if text == '유튜브':
        await message.channel.send('https://www.youtube.com/channel/UCjT8TO5nfj5joncCF-q_iNg/featured')
    if text == '뮤트 반란죄수':
        await message.channel.send('반란죄수님을 뮤트하는중..')
    if text == '시스템 체크':
        await message.channel.send('시스템체크에 실패했습니다!') 
    if text == '베타시스템 사용':
        await message.channel.send('베타코드 10자리를 입력해주세요!') 
    if text == '미니게임 시작':
        await message.channel.send('미니게임을 선택해주세요! [도박, 가위바위보]') 
    if text == '후원':
        await message.channel.send("https://toon.at/donate/637289109677063079, https://twip.kr/chaos_insurgency1 후원링크에요!")
    if text == '영상':
        await message.channel.send("https://youtu.be/BJSPvGlm1Hg")
    if text == '15Dkdoac02':
        await message.channel.send("베타테스팅 기능이 정상적으로 활성화 되었습니다.")      
    if text == '반란죄수봇아 박제한거 [1] 보여줘':
        await message.channel.send("https://cdn.discordapp.com/attachments/726701376100368464/727497748731133992/image0.jpg  반란죄수 : 난 똑똑한 여자야")  
    if text == '인증된 서버 공지':
        await client.get_channel(726820608918421554).send('경고 I Warning 봇 메인 시스템과 연결이 종료되었습니다. 리로드중..')  
    if message.content == "타이머":
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}님 10초가 지났어요!")
    if text == 'ㅇㅅㅇ':
        await message.channel.send('ㅎㅅㅎ') 
    if message.content.startswith("!채팅청소"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[6:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(f"**{amount}**개의 메시지를 지웠습니다.")
            except ValueError:
                await message.channel.send("청소하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send("권한이 없습니다.")
    if text == '!임베드':
        embed=discord.Embed(color=0xff00, title="방송안내", description= "입력 대기중입니다.", timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if text == '!임베드 [경고]':
        embed=discord.Embed(color=0xff00, title="반란죄수 warning logs", description= "처벌 수위 : inf정지", timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    if text == "가위바위보 하기" or text == "가위바위보" or text == "가위 바위 보":
        await message.channel.send("가위바위보 가위 , 가위바위보 바위 , 가위바위보 보 처럼 입력해주세요!")
    if text == "가위바위보 가위" or text == "가위바위보 바위" or text == "가위바위보 보":
        #이기게 될 경우의 수는
        #사(사람):가위 봇:보, 사:바위 봇:가위 , 사:보 봇:바위 
        #총 3개

        #실패 될 경우의 수는
        #사:보 봇:가위, 사:가위 봇:바위 , 사:바위 봇:보
        #총 3개

        #비길 경우의 수
        #사:보 봇:보 , 사:가위 봇:가위 , 사: 바위 봇:바위
        #총 3개

        #그러므로 성공,실패,비김 을 비율로 나타낼 때 1:1:1 로 나타낼수 있다는것을 알수 있다
        #그러므로 그냥 랜덤 1~3 을 만들고 1이면 이김, 2 면 짐 , 3이면 비김으로 처리하면 될것이다
        bot_response = random.randint(1, 3)
        #다음과 같이 나타날수 있을것이다
        if bot_response == 1:
            await message.channel.send("이겼습니다!")
        elif bot_response == 2:
            await message.channel.send("이런... 졌습니다")
        elif bot_response == 3:
            await message.channel.send("비겼습니다!")
    if text == "도박하기" or text == "도박" or text == "4달라":
        await message.channel.send("추첨중...")
    if text == "도박하기" or text == "도박" or text == "4달라":
        #이기게 될 경우의 수는
        #사(사람):가위 봇:보, 사:바위 봇:가위 , 사:보 봇:바위 
        #총 3개

        #실패 될 경우의 수는
        #사:보 봇:가위, 사:가위 봇:바위 , 사:바위 봇:보
        #총 3개

        #비길 경우의 수
        #사:보 봇:보 , 사:가위 봇:가위 , 사: 바위 봇:바위
        #총 3개

        #그러므로 성공,실패,비김 을 비율로 나타낼 때 1:1:1 로 나타낼수 있다는것을 알수 있다
        #그러므로 그냥 랜덤 1~3 을 만들고 1이면 이김, 2 면 짐 , 3이면 비김으로 처리하면 될것이다
        bot_response = random.randint(1, 8)
        #다음과 같이 나타날수 있을것이다
        if bot_response == 1:
            await message.channel.send("블랙카드가 나왔어요!!!")
        elif bot_response == 2:
            await message.channel.send("카드같은건 없어요^^")
        elif bot_response == 3:
            await message.channel.send("함정카드 발동!!!")
        elif bot_response == 4:
            await message.channel.send("당신은 카드를 훔칠려다 레일건을 맞고 사망하셨습니다.")
        elif bot_response == 5:
            await message.channel.send("과학자 카드가 나왔네요!")
        elif bot_response == 6:
            await message.channel.send("수석 과학자 카드가 나왔네요!")
        elif bot_response == 7:
            await message.channel.send("구역 관리자 카드가 나왔어요!")
        elif bot_response == 8:
            await message.channel.send("격리기사 카드가 나왔어요!")
    if text == "총 뽑기" or text == "총을 뽑자" or text == "반란하고 싶다":
        await message.channel.send("추첨중...")
    if text == "총뽑기" or text == "총을 뽑자" or text == "반란하고 싶다":
        #이기게 될 경우의 수는
        #사(사람):가위 봇:보, 사:바위 봇:가위 , 사:보 봇:바위 
        #총 3개

        #실패 될 경우의 수는
        #사:보 봇:가위, 사:가위 봇:바위 , 사:바위 봇:보
        #총 3개

        #비길 경우의 수
        #사:보 봇:보 , 사:가위 봇:가위 , 사: 바위 봇:바위
        #총 3개

        #그러므로 성공,실패,비김 을 비율로 나타낼 때 1:1:1 로 나타낼수 있다는것을 알수 있다
        #그러므로 그냥 랜덤 1~3 을 만들고 1이면 이김, 2 면 짐 , 3이면 비김으로 처리하면 될것이다
        bot_response = random.randint(1, 8)
        #다음과 같이 나타날수 있을것이다
        if bot_response == 1:
            await message.channel.send("정의의 로지카가 나왔어요!!!")
        elif bot_response == 2:
            await message.channel.send("오 레일건이 나왔네요!")
        elif bot_response == 3:
            await message.channel.send("USP획득!")
        elif bot_response == 4:
            await message.channel.send("당신은 총을 훔칠려다 가드의 MP7에 맞고 사망하셨습니다.")
        elif bot_response == 5:
            await message.channel.send("엡실론이 나왔어요!")
        elif bot_response == 6:
            await message.channel.send("P90이 나왔네요~!")
        elif bot_response == 7:
            await message.channel.send("탄약이 나왔어요")
        elif bot_response == 8:
            await message.channel.send("총을 먹으려다 댕댕이에게 먹혔군요..")

client.run(token)



