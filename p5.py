n;
	int dif = sum - m;
	ll ans = 0;
	ll mul = 1;
	while (x > 0)
	{
		y = x % 10;
		if (mul > 1) y++;


		if (dif <= 0) {
			ans += max(0, abs(dif) - 1);
			break;
		}
		else
		{
			dif = dif - y;
			y = 10 - y;
			y = mul * y;
			ans += y;
		}
		mul = mul * 10;
		x /= 10;
	}

	cout << ans << endl;
}







int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	PEACE
	ll t = 1;
	ll ct = 1;
	cin >> t;
	while (ct 
