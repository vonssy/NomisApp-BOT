from aiohttp import (
    ClientResponseError,
    ClientSession,
    ClientTimeout
)
from datetime import datetime, timezone
from fake_useragent import FakeUserAgent
from colorama import *
import asyncio, json, urllib.parse, os, pytz

wib = pytz.timezone('Asia/Jakarta')

class NomisApp:
    def __init__(self) -> None:
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'cms-api.nomis.cc',
            'Origin': 'https://telegram.nomis.cc',
            'Pragma': 'no-cache',
            'Referer': 'https://telegram.nomis.cc/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': FakeUserAgent().random
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}NomisApp - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def load_data(self, query: str):
        query_params = urllib.parse.parse_qs(query)
        query = query_params.get('user', [None])[0]

        if query:
            user_data_json = urllib.parse.unquote(query)
            user_data = json.loads(user_data_json)

            return {
                'referrer': 'lqJ0Cdwq76',
                'telegram_user_id': user_data['id'],
                'telegram_username': user_data.get('username', '')
            }
        else:
            raise ValueError("User data not found in query.")

    async def user_auth(self, query: str, retries=3):
        url = 'https://cms-api.nomis.cc/api/users/auth'
        data = json.dumps(self.load_data(query))
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json',
            'X-App-Init-Data': query
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
    
    async def refferal_data(self, query: str, retries=3):
        url = 'https://cms-api.nomis.cc/api/users/referrals-data'
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'X-App-Init-Data': query
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
                
    async def claim_refferal(self, query: str, retries=3):
        url = 'https://cms-api.nomis.cc/api/users/claim-referrals'
        headers = {
            **self.headers,
            'Content-Length': '2',
            'Content-Type': 'application/json',
            'X-App-Init-Data': query
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, json={}) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None

    async def farm_data(self, query: str, retries=3):
        url = 'https://cms-api.nomis.cc/api/users/farm-data'
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'X-App-Init-Data': query
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
                
    async def start_farm(self, query: str, retries=3):
        url = 'https://cms-api.nomis.cc/api/users/start-farm'
        headers = {
            **self.headers,
            'Content-Length': '2',
            'Content-Type': 'application/json',
            'X-App-Init-Data': query
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, json={}) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
                
    async def claim_farm(self, query: str, retries=3):
        url = 'https://cms-api.nomis.cc/api/users/claim-farm'
        headers = {
            **self.headers,
            'Content-Length': '2',
            'Content-Type': 'application/json',
            'X-App-Init-Data': query
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, json={}) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result["result"]
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
                
    async def claim_farm_bonus(self, query: str, retries=3):
        url = 'https://cms-api.nomis.cc/api/users/claim-farm'
        data = json.dumps({'isUseFriendsBonus':True})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json',
            'X-App-Init-Data': query
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        response.raise_for_status()
                        result = await response.json()
                        return result["result"]
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
                
    async def tasks_data(self, query: str, retries=3):
        url = 'https://cms-api.nomis.cc/api/users/tasks'
        headers = {
            **self.headers,
            'Content-Type': 'application/json',
            'X-App-Init-Data': query
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.get(url=url, headers=headers) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None
                
    async def claim_tasks(self, query: str, sub_task_id: int, retries=3):
        url = 'https://cms-api.nomis.cc/api/users/claim-task'
        data = json.dumps({'task_id':sub_task_id})
        headers = {
            **self.headers,
            'Content-Length': str(len(data)),
            'Content-Type': 'application/json',
            'X-App-Init-Data': query
        }
        for attempt in range(retries):
            try:
                async with ClientSession(timeout=ClientTimeout(total=20)) as session:
                    async with session.post(url=url, headers=headers, data=data) as response:
                        print(response.status, await response.text())
                        response.raise_for_status()
                        result = await response.json()
                        return result['data']['result']
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}ERROR.{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying.... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(2)
                else:
                    return None

    async def process_query(self, query: str):
        user = await self.user_auth(query)
        if not user:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Query ID Isn't Valid {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        farm_data = await self.farm_data(query)
        if not farm_data:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Query ID Isn't Valid {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if user and farm_data:
            self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {user['telegramUsername']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                f"{Fore.WHITE+Style.BRIGHT} {farm_data['points'] / 1000} Points {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            await asyncio.sleep(1)

            refferal = await self.refferal_data(query)
            if refferal:
                points = refferal['claimAvailable'] / 1000
                next_reff_claim = refferal['nextReferralsClaimAt']

                if points > 0:
                    if next_reff_claim is None:
                        claim = await self.claim_refferal(query)
                        if claim:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {points} Points {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                    else:
                        now = datetime.now(timezone.utc)
                        next_reff_claim_utc = datetime.strptime(next_reff_claim, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
                        next_reff_claim_wib = next_reff_claim_utc.astimezone(wib).strftime('%x %X %Z')

                        if now >= next_reff_claim_utc:
                            claim = await self.claim_refferal(query)
                            if claim:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {points} Points {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} Not Time to Claim {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Next Claim at{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {next_reff_claim_wib} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} No Available Reward to Claim {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
            )
            await asyncio.sleep(1)

            next_farm_claim = farm_data['nextFarmClaimAt']
            if next_farm_claim is None:
                start = await self.start_farm(query)
                if start:
                    next_farm_claim_utc = datetime.strptime(start['next_farm_claim_at'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
                    next_farm_claim_wib = next_farm_claim_utc.astimezone(wib).strftime('%x %X %Z')
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {next_farm_claim_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                await asyncio.sleep(1)

            else:
                now = datetime.now(timezone.utc)
                next_farm_claim_utc = datetime.strptime(next_farm_claim, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
                next_farm_claim_wib = next_farm_claim_utc.astimezone(wib).strftime('%x %X %Z')

                if now >= next_farm_claim_utc:
                    claim = await self.claim_farm(query)
                    if claim:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {farm_data['pointsPerClaim'] / 1000} Points {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                        await asyncio.sleep(1)

                        start = await self.start_farm(query)
                        if start:
                            next_farm_claim_utc = datetime.strptime(start['next_farm_claim_at'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
                            next_farm_claim_wib = next_farm_claim_utc.astimezone(wib).strftime('%x %X %Z')
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.GREEN+Style.BRIGHT} Is Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {next_farm_claim_wib} {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )
                        else:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )

                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Not Time to Claim {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {next_farm_claim_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                await asyncio.sleep(1)

                farm_bonus = user['inviteFriend']
                if farm_bonus:
                    bonus = farm_bonus['bonus']
                    count = farm_bonus['usageCount']
                    max_count = farm_bonus['pricePerUsage']

                    if bonus is not None and bonus >= max_count:
                        while count < max_count:
                            if count == max_count:
                                break

                            if bonus < max_count:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming Bonus{Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reason{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} Not Eligible {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                break
                            
                            claim = await self.claim_farm_bonus(query)
                            if claim:
                                count += 1
                                bonus -= max_count
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming Bonus{Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} 35.0 Points {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}] [ Chance{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {count}/{max_count} {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Farming Bonus{Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                                break
                            
                            await asyncio.sleep(1)

                        if count == max_count:
                            self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Farming Bonus{Style.RESET_ALL}"
                                f"{Fore.YELLOW+Style.BRIGHT} No Available Chance {Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                            )

                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Farming Bonus{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Not Eligible to Claim {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Farming Bonus{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                await asyncio.sleep(1)

                tasks = await self.tasks_data(query)
                if tasks:
                    completed = False
                    for task in tasks:
                        if task:
                            completed_sub = False
                            title = task['title']
                            sub_tasks = task['ton_twa_tasks']

                            for sub_task in sub_tasks:
                                sub_task_id = sub_task['id']

                                if sub_task:
                                    claim = await self.claim_tasks(query, sub_task_id)
                                    if claim:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {sub_task['title']} {Style.RESET_ALL}"
                                            f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {sub_task['reward'] / 1000} Points {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                        )
                                    else:
                                        self.log(
                                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT}-{Style.RESET_ALL}"
                                            f"{Fore.WHITE+Style.BRIGHT} {sub_task['title']} {Style.RESET_ALL}"
                                            f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                            f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                        )
                                    await asyncio.sleep(1)

                                else:
                                    completed_sub = True

                            if completed_sub:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {title} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Completed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            await asyncio.sleep(1)

                        else:
                            completed = True

                    if completed:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )

                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Task{Style.RESET_ALL}"
                        f"{Fore.GREEN+Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )

                
    async def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        await self.process_query(query)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        await asyncio.sleep(3)
                        

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    await asyncio.sleep(1)
                    seconds -= 1

        except FileNotFoundError:
            self.log(f"{Fore.RED}File 'query.txt' tidak ditemukan.{Style.RESET_ALL}")
            return
        except Exception as e:
            self.log(f"{Fore.RED+Style.BRIGHT}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        bot = NomisApp()
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
            f"{Fore.RED + Style.BRIGHT}[ EXIT ] Nomis App - BOT{Style.RESET_ALL}",                                       
        )