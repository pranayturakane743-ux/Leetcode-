public class Solution
{
    public int MyAtoi(string s)
    {
        int i = 0;
        int n = s.Length;

        while (i < n && s[i] == ' ')
            i++;

  
        int sign = 1;
        if (i < n && (s[i] == '+' || s[i] == '-'))
        {
            if (s[i] == '-')
                sign = -1;
            i++;
        }

        long result = 0;

        while (i < n && char.IsDigit(s[i]))
        {
            result = result * 10 + (s[i] - '0');

            if (sign * result > int.MaxValue)
                return int.MaxValue;

            if (sign * result < int.MinValue)
                return int.MinValue;

            i++;
        }

        return (int)(sign * result);
    }
}