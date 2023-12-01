#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>

int	main()
{
	{
		std::ifstream	file("input.txt");
		std::string		line;
		int				sum = 0;

		if (!file.is_open())
		{
			std::cerr << "Error opening file" << std::endl;
			return (1);
		}

		while (std::getline(file, line))
		{
			size_t	start;
			size_t	end;

			start = line.find_first_of("123456789");
			end = line.find_last_of("123456789");

			if (start == std::string::npos || end == std::string::npos)
			{
				std::cerr << "Error finding numbers in line" << std::endl;
				return (1);
			}
			sum += std::stoi(line.substr(start, 1) + line.substr(end, 1));
		}

		std::cout << "Part 1 output =  " << sum << std::endl;
		file.close();
	}
	{
		std::ifstream	file("input.txt");
		std::string		line;
		int				sum = 0;

		if (!file.is_open())
		{
			std::cerr << "Error opening file" << std::endl;
			return (1);
		}

		std::map<int, std::string> words = {
			{1, "one"},
			{2, "two"},
			{3, "three"},
			{4, "four"},
			{5, "five"},
			{6, "six"},
			{7, "seven"},
			{8, "eight"},
			{9, "nine"}
		};

		while (std::getline(file, line))
		{
			std::vector<std::string>	numbers;
			size_t						i = 0;

			while (i < line.size())
			{
				if (isdigit(line[i]))
					numbers.push_back(line.substr(i,1));
				for (const auto& [index, word] : words)
				{
					if (line.substr(i, word.size()) == word)
					{
						numbers.push_back(std::to_string(index));
						break;
					}
				}
				i++;
			}
			sum += std::stoi(numbers.front() + numbers.back());
		}

		std::cout << "Part 2 output =  " << sum << std::endl;
		file.close();
	}
	return (0);
}
